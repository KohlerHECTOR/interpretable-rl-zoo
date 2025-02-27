import numpy as np
from itertools import chain
from ocatari.ram.extract_ram_info import (
    detect_objects_ram, init_objects, get_max_objects, get_object_state_size, get_class_dict)
from ocatari.vision.extract_vision_info import detect_objects_vision
from ocatari.vision.utils import mark_bb, to_rgba
from ocatari.ram.game_objects import GameObject, ValueObject
from ocatari.utils import draw_label, draw_arrow
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.env_util import make_atari_env

from huggingface_sb3 import load_from_hub
from stable_baselines3.common.vec_env import VecNormalize, DummyVecEnv
import gymnasium as gym


try:
    # ALE (Arcade Learning Environment) is required for running Atari environments.
    import ale_py
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        '\nALE is required when using the ALE env wrapper. Try `pip install "gymnasium[atari, accept-rom-license]"`\n')

try:
    # OpenCV is used for processing frames for observation (e.g., resizing, grayscaling)
    import cv2
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        '\nOpenCV is required when using the ALE env wrapper. Try `pip install opencv-python`.')

try:
    import pygame  # Pygame is required for rendering the environment for human visualization
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        '\npygame is required for human rendering. Try `pip install pygame`.')

# List of available games for the OCAtari environment
AVAILABLE_GAMES = [
    "Adventure", "AirRaid", "Alien", "Amidar", "Assault", "Asterix", "Asteroids", "Atlantis", "BankHeist", "BattleZone",
    "BeamRider", "Berzerk", "Bowling", "Boxing", "Breakout", "Carnival", "Centipede", "ChopperCommand", "CrazyClimber",
    "DemonAttack", "DonkeyKong", "DoubleDunk", "Enduro", "FishingDerby", "Freeway", "Frogger", "Frostbite", "Galaxian",
    "Gopher", "Hero", "IceHockey", "Jamesbond", "Kangaroo", "KeystoneKapers", "KingKong", "Krull", "KungFuMaster",
    "MarioBros", "MontezumaRevenge", "MsPacman", "NameThisGame", "Pacman", "Phoenix", "Pitfall", "Pong", "Pooyan",
    "PrivateEye", "Qbert", "Riverraid", "RoadRunner", "Seaquest", "Skiing", "SpaceInvaders", "StarGunner",
    "Tennis", "TimePilot", "UpNDown", "Venture", "VideoPinball", "YarsRevenge", "Zaxxon"
]

# Constant to control the upscaling factor for rendering
UPSCALE_FACTOR = 5


# The OCAtari environment provides an interface to interact with Atari 2600 games through Gymnasium, enabling object tracking and analysis. This environment extends the functionality of traditional Atari environments by incorporating different object detection modes (RAM, vision, or both) and supports enhanced observation spaces for advanced tasks like reinforcement learning.
class OCAtariDQN:
    """
    :param env_name: The name of the Atari gymnasium environment e.g. "Pong" or "PongNoFrameskip-v5"
    :type env_name: str
    :param mode: The detection method type: one of `raw`, `ram`, `vision`, or `both` (i.e. `ram` + `vision`)
    :type mode: str
    :param hud: Whether to include or not objects from the HUD (e.g. scores, lives)
    :type hud: bool
    :param obs_mode: Define the observation mode. Set to `dqn` (84x84, grayscaled), `ori` (210x160x3, RGB image), `obj` (#Objectsx4). `dqn` and `ori` are also organized in a stack of the last 4 frames.
    :type obs_mode: str
    :param buffer_window_size: The size of the buffer window for observation stacks.
    :type buffer_window_size: int
    :param create_buffer_stacks: Decide what stacks you want to create. The obs_mode automatically add the fitting stack itself. Add "dqn" or "obj" if you want additional stacks.
    :type create_buffer_stacks: list

    The remaining \*args and \**kwargs will be passed to the `gymnasium.make` function.
    """

    def __init__(self, env_name, render_mode=None):
        # Determine the game name and check if it's supported
        game_name = env_name.split("/")[1].split("-")[0].split("No")[0].split("Deterministic")[
            0] if "ALE/" in env_name else env_name.split("-")[0].split("No")[0].split("Deterministic")[0]
        if game_name[:4] not in [gn[:4] for gn in AVAILABLE_GAMES]:
            raise ValueError(f"Game '{env_name}' not covered yet by OCAtari")

        # Store initialization parameters
        self.env_name = env_name
        self.game_name = game_name
        self.hud = True  # to match vision
        self.render_mode = render_mode

        # Create vectorized environment with proper preprocessing
        vec_env = make_atari_env(env_name, n_envs=1, env_kwargs={"render_mode": render_mode}, seed=0,
                                 wrapper_kwargs={"terminal_on_life_loss": False})
        self._env = VecFrameStack(vec_env, n_stack=4)

        # Define observation space based on the observation mode

        # Set up object tracking and observation properties
        self.max_objects_per_cat = get_max_objects(self.game_name, self.hud)
        self._class_dict = get_class_dict(self.game_name)
        self._slots = [self._class_dict[c]() for c, n in self.max_objects_per_cat.items() for _ in range(n)]
        self._ns_state = np.zeros(sum([len(o._nsrepr) for o in self._slots]))
        self.ns_meaning = [f"{o.category} ({o._ns_meaning})" for o in self._slots]
        self.observation_space = gym.spaces.Box(
            0, 255.0, (get_object_state_size(self.game_name, self.hud) + len(self._ns_state),))
        print(self._ns_state, self.ns_meaning)
        self.action_space = self._env.action_space

        # Get ALE interface from the base environment
        self._ale = self._env.envs[0].unwrapped.ale

        # Set up object detection methods
        # Ram only
        self.detect_objects = self._detect_objects_ram
        self.objects = init_objects(self.game_name, self.hud)

        self.rendering_initialized = False

    def step(self, action):
        # Step the vectorized environment
        obs, reward, terminated, info = self._env.step([action])  # VecEnv expects a list of actions
        # Update object detection and buffers
        self.detect_objects()

        info[0]["dqn_state"] = obs[0]
        # VecEnv doesn't have truncated, so we use False as default
        truncated = False
        new_s = np.array(self.ns_state)
        stot = np.concatenate((new_s, new_s - self.last_viewed))
        self.last_viewed = new_s
        return stot, reward[0], truncated, terminated[0], info[0]

    def reset(self, **kwargs):
        # Reset the vectorized environment
        obs = self._env.reset()

        # Reset object detection and buffers
        self.objects = init_objects(self.game_name, self.hud, vision=False)
        self.detect_objects()
        self.last_viewed = np.array(self.ns_state)
        return np.concatenate((self.last_viewed, np.zeros_like(self.last_viewed))), {"dqn_state": obs[0]}

    def _detect_objects_ram(self):
        # Detect objects using RAM-based extraction from the vectorized environment
        detect_objects_ram(
            self.objects, self._ale.getRAM(), self.game_name, self.hud)

    def _detect_objects_vision(self):
        # Detect objects using vision-based extraction from the vectorized environment
        detect_objects_vision(
            self.objects, self._ale.getScreenRGB(), self.game_name, self.hud)

    def _detect_objects_both(self):
        # Use both RAM and vision-based extraction methods to detect objects
        detect_objects_ram(
            self.objects, self._ale.getRAM(), self.game_name, self.hud)
        detect_objects_vision(
            self.objects_v, self._ale.getScreenRGB(), self.game_name, self.hud)

    def _reset_buffer(self):
        # Reset the buffer by filling it with the initial states
        for _ in range(self.buffer_window_size):
            self._fill_buffer()

    def _fill_buffer(self):
        # Fill the RGB, DQN, and neurosymbolic state buffers with the current states
        if self.create_dqn_stack:
            dqn_obs = cv2.resize(cv2.cvtColor(self._ale.getScreenRGB(
            ), cv2.COLOR_RGB2GRAY), (84, 84), interpolation=cv2.INTER_AREA)
            self._state_buffer_dqn.append(dqn_obs)
        if self.create_rgb_stack:
            self._state_buffer_rgb.append(self._ale.getScreenRGB())
        if self.create_ns_stack:
            self._state_buffer_ns.append(self._ns_state)

    window: pygame.Surface = None
    clock: pygame.time.Clock = None

    def _initialize_rendering(self, sample_image):
        # Initialize rendering with Pygame using a sample image to determine size
        assert sample_image is not None
        pygame.init()
        if self.render_mode == "human":
            pygame.display.set_caption(self.game_name)
        self.image_size = (sample_image.shape[1], sample_image.shape[0])
        # render with higher res
        self.window_size = (
            sample_image.shape[1] * UPSCALE_FACTOR, sample_image.shape[0] * UPSCALE_FACTOR)
        self.label_font = pygame.font.SysFont('Pixel12x10', 16)
        if self.render_mode == "human":
            self.window = pygame.display.set_mode(self.window_size)
            self.clock = pygame.time.Clock()
        else:
            self.window = pygame.Surface(self.window_size)
        self.rendering_initialized = True

    def render(self, image=None):
        """
        Compute the render frames (as specified by render_mode during the initialization of the environment).
        If activated, adds an overlay visualizing object properties like position, velocity vector, name, etc.
        """
        # Render the environment image

        if image is None:
            image = self._env.render()

        if not self.render_oc_overlay:
            if self.rendering_initialized:
                # Upscale and return the rendered image
                return image.swapaxes(0, 1).repeat(UPSCALE_FACTOR, axis=0).repeat(UPSCALE_FACTOR, axis=1)
            return image
        if not self.rendering_initialized:
            self._initialize_rendering(image)

        # Prepare the image surface for rendering
        image = np.transpose(image, (1, 0, 2))
        image_surface = pygame.Surface(self.image_size)
        pygame.pixelcopy.array_to_surface(image_surface, image)
        upscaled_image = pygame.transform.scale(
            image_surface, self.window_size)
        self.window.blit(upscaled_image, (0, 0))

        # Overlay surface for additional visualizations like bounding boxes
        overlay_surface = pygame.Surface(self.window_size)
        overlay_surface.set_colorkey((0, 0, 0))

        # Draw detected objects as bounding boxes with labels
        for game_object in self.objects:
            x, y = game_object.xy
            w, h = game_object.wh

            if x == np.nan:
                continue

            # Scale object properties for rendering
            dx, dy = game_object.dx * UPSCALE_FACTOR, game_object.dy * UPSCALE_FACTOR
            x, y, w, h = x * UPSCALE_FACTOR, y * UPSCALE_FACTOR, w * \
                         UPSCALE_FACTOR, h * UPSCALE_FACTOR
            x_c, y_c = x + w // 2, y + h // 2

            # Draw bounding box
            pygame.draw.rect(
                overlay_surface, color=game_object.rgb, rect=(x, y, w, h), width=2)
            # Draw label with object category
            label = game_object.category
            if isinstance(game_object, ValueObject):
                label += f" ({game_object.value})"
            draw_label(self.window, label, position=(
                x, y + h + 4), font=self.label_font)
            # Draw velocity vector if applicable
            if dx != 0 or dy != 0:
                draw_arrow(overlay_surface, start_pos=(float(x_c), float(y_c)), end_pos=(
                    x_c + 2 * dx, y_c + 2 * dy), color=(100, 200, 255), width=2)

        self.window.blit(overlay_surface, (0, 0))

        # Update the display for human rendering or return the image array for rgb_array mode
        if self.render_mode == "human":
            frameskip = self._env.envs[0].unwrapped._frameskip if isinstance(
                self._env.envs[0].unwrapped._frameskip, int) else 1
            self.clock.tick(60 // frameskip)
            pygame.display.flip()
            pygame.event.pump()
        elif self.render_mode == "rgb_array":
            return pygame.surfarray.array3d(self.window)

    def close(self, *args, **kwargs):
        """
        Close the environment and perform cleanup.
        """
        return self._env.close(*args, **kwargs)

    def seed(self, seed, *args, **kwargs):
        # Set the random seed for reproducibility
        self._env.seed(seed, *args, **kwargs)

    def getScreenRGB(self):
        """
        Returns the current RGB screen state of the environment.

        :return: A NumPy array representing the RGB screen state.
        :rtype: np.array
        """
        return self._ale.getScreenRGB()

    @property
    def nb_actions(self):
        """
        The number of actions available in this environment.
        """
        return self.action_space.n

    @property
    def get_rgb_state(self):
        """
        Returns the current RGB state of the environment.
        """
        return self._ale.getScreenRGB()

    def set_ram(self, target_ram_position, new_value):
        """
        Directly set a given value at a targeted RAM position.
        """
        return self._env.envs[0].unwrapped.ale.setRAM(target_ram_position, new_value)

    def get_ram(self):
        """
        Returns the RAM state.
        """
        return self._ale.getRAM()

    def get_action_meanings(self):
        # Return the meanings of each action
        return self._env.envs[0].env.env.get_action_meanings()

    def _get_obs(self):
        # Get the current observation from the environment
        return self._env.envs[0].env.env.unwrapped._get_obs()

    def detect_objects_both(self):
        # Use both RAM and vision-based methods to detect objects
        self._detect_objects_ram()
        self._detect_objects_vision()

    def _clone_state(self):
        """
        Returns the current system state of the environment.
        """
        return self._env.envs[0].env.env.ale.cloneSystemState()

    def _restore_state(self, state):
        """
        Restore the system state of the environment.
        """
        return self._env.envs[0].env.env.ale.restoreSystemState(state)

    @property
    def ns_state(self):
        """
        Returns the current neurosymbolic state of the environment.
        """
        return list(chain.from_iterable([o._nsrepr for o in self.objects]))

    def render_explanations(self):
        # Render explanations by highlighting the objects with bounding boxes
        rendered = np.zeros_like(self._state_buffer_rgb[0]).astype(float)
        coefs = [0.05, 0.1, 0.25, 0.6]
        for coef, state_i in zip(coefs, self._state_buffer_rgb):
            rendered += coef * state_i
        rendered = rendered.astype(int)
        for obj in self.objects:
            mark_bb(rendered, obj.xywh, color=obj.rgb)
        import matplotlib.pyplot as plt
        plt.imshow(rendered)
        rows, cells, colors = [], [], []
        columns = ["X, Y", "W, H", "R, G, B"]
        for obj in self.objects:
            rows.append(obj.category)
            cells.append([obj.xy, obj.wh, obj.rgb])
            colors.append(to_rgba(obj.rgb))
        t_height = 0.03 * len(rows)
        table = plt.table(cellText=cells, rowLabels=rows, rowColours=colors, colLabels=columns,
                          colWidths=[.2, .2, .3], bbox=[0.1, 1.02, 0.8, t_height], loc='top')
        table.set_fontsize(14)
        plt.subplots_adjust(top=0.8)
        plt.show()

    def aggregated_render(self, coefs=[0.05, 0.1, 0.25, 0.6]):
        # Generate a weighted sum of frames for a more informative representation
        rendered = np.zeros_like(self._state_buffer_rgb[0]).astype(float)
        for coef, state_i in zip(coefs, self._state_buffer_rgb):
            rendered += coef * state_i
        rendered = rendered.astype(int)
        return rendered

class Unvec(gym.Env):
    def __init__(self, vec_env: DummyVecEnv, render_mode: str = None, env_name:str = None):
        self.env = vec_env
        self.render_mode = self.env.envs[0].render_mode
        self.observation_space = self.env.envs[0].observation_space
        self.action_space = self.env.envs[0].action_space
        self.env_name = env_name
        # self.env.envs[0].ocatari_env._env.render_mode=render_mode

    def reset(self, *args, **kwargs):
        return self.env.reset()[0], {}

    def step(self, action):
        s, r, done, infos = self.env.step([action])
        terminated = infos[0].get("terminal_observation") is not None
        truncated = infos[0]["TimeLimit.truncated"]
        return s[0], r[0], terminated, truncated, infos[0]

    def render(self):
        return self.env.envs[0].render()

def load_env_from_hf(env_name, algo="PPO", **kwargs):
    """
    Load a pre-trained policy from Hugging Face Hub.

    Args:
        env_name: Gym environment
        algo: Algorithm to use ("PPO", "SAC", or "DQN")
        load_replay_buffer: Whether to attempt loading the replay buffer

    Returns:
        Loaded policy
    """
    # if env_name in ["ME", "CSTR", "cryst", "4tank"]:
    #     assert algo == "SAC"
    #     model = SAC.load(f"processes_policies/SAC_{env_name}_rep_0.zip", device='cpu')
    #     env = load_process_env(env_name)
    #     return model, env

    if algo not in ["PPO", "SAC", "DQN"]:
        raise ValueError(f"Algorithm {algo} not supported. Choose from PPO, SAC, or DQN")

    try:
        # Get the algorithm class
        repo_id = f"sb3/{algo.lower()}-{env_name}"

        if env_name in ["Ant-v3", "Swimmer-v3", "Walker2d-v3", "Humanoid-v3", "Hopper-v3", "HalfCheetah-v3"]:
            env_name = env_name.split("-")[0] + "-v4"

        # Try to load normalization stats if they exist
        try:
            normalize_path = load_from_hub(
                repo_id=repo_id,
                filename="vec_normalize.pkl"
            )
            if env_name == "Hopper-v4":
                env = DummyVecEnv([lambda: gym.make(env_name, healthy_angle_range=(-0.24, 0.24), **kwargs)])
            elif env_name == "BipedalWalkerHardcore-v3":
                env = DummyVecEnv([lambda: gym.make(env_name, hardcore=True, **kwargs)])
            else:
                env = DummyVecEnv([lambda: gym.make(env_name, **kwargs)])
            env = VecNormalize.load(normalize_path, env)
            env.training = False  # Disable training mode
            env.norm_reward = False  # Disable reward normalization
            env = Unvec(env, env_name=env_name)
        except Exception:
            # If normalization stats don't exist, create regular environment
            if "NoFrameskip" in env_name:
                env = OCAtariDQN(env_name, **kwargs)
            elif env_name == "BipedalWalkerHardcore-v3":
                env = gym.make(env_name, hardcore=True, **kwargs)
            elif env_name == "Hopper-v4":
                env = gym.make(env_name, healthy_angle_range=(-0.24, 0.24), **kwargs)
            else:
                env = gym.make(env_name, **kwargs)
        return env


    except Exception as e:
        raise Exception(f"Failed to load model from {repo_id}: {str(e)}")