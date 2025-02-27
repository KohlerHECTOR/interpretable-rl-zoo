import inspect

from interpretable_rl_zoo.utils import load_policy_from_hf


def make_env_from_metadata(metadata: dict, **kwargs):
    _, env = load_policy_from_hf(metadata["env_name"], metadata["algorithm"], **kwargs)
    return env

def print_policy(module):
    print(f"The policy {module.__name__} is trained from the algorithm {module.metadata['algorithm']} in environment {module.metadata['env_name']}.")
    print(f"The policy is defined by the function:\n{inspect.getsource(module.play)}")
