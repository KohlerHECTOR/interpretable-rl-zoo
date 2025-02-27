from interpretable_rl_zoo import make_env_from_metadata, print_policy
import  interpretable_rl_zoo.policy.cart_pole.tree_small as tree_policy

if __name__ == '__main__':
    env = make_env_from_metadata(tree_policy.metadata, render_mode="human")

    observation, info = env.reset()
    done = False
    total_reward = 0

    print_policy(tree_policy)

    while not done:
        action = tree_policy.play(observation)

        observation, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        total_reward += reward

    print(f"Episode finished with total reward: {total_reward}")
    env.close()
