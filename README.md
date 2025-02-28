# Interpretable Reinforcement Learning Zoo
**TESTED ON PYTHON 3.10**
A collection of human-understandable reinforcement learning policies implemented as simple Python scripts. This library provides interpretable versions of complex RL policies, making them accessible for educational purposes and research.

## Overview

The Interpretable RL Zoo contains policies that have been distilled from the [Stable-Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo) experts into various interpretable policy classes:
- Decision Trees
- Oblique Trees
- Multi-Layer Perceptrons (MLPs)
- Linear

Policy have multiple sizes (number of parameters):
- Tiny
- Small
- Medium
- Large
- Huge
- Mega

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Here's a simple example of how to use a tree policy for the Pong environment, that can be found in the `example.py` file:

```python
from interpretable_rl_zoo import make_env_from_metadata, print_policy
import interpretable_rl_zoo.policy.pong_no_frameskip.tree_huge as tree_policy

if __name__ == '__main__':
    # Create environment based on policy metadata
    env = make_env_from_metadata(tree_policy.metadata, render_mode="human")
    
    # Reset environment
    observation, info = env.reset()
    done = False
    total_reward = 0
    
    # Print the policy structure for better understanding
    print_policy(tree_policy)
    
    # Run the policy
    while not done:
        action = tree_policy.play(observation)
        observation, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        total_reward += reward
    
    print(f"Episode finished with total reward: {total_reward}")
    env.close()
```

## Policy Structure

All policies are located in the `interpretable_rl_zoo/policy` directory, organized by environment:

```
interpretable_rl_zoo/policy/
├── pong_no_frameskip/
│   ├── tree_small.py
│   ├── ...
│   └── mlp_large.py
├── cartpole/
│   ├── ...
├── lunar_lander/
│   ├── ...
└── ...
```

Each policy file contains:
1. A `metadata` dictionary that provides info about the source algoritihm and environments.
2. A `play(observation)` function that maps observations to actions

## Understanding Policies

You can visualize and understand any policy using the `print_policy` function:

```python
from interpretable_rl_zoo import print_policy
import interpretable_rl_zoo.policy.cartpole.tree_small as policy

print_policy(policy)
```

This will output a human-readable representation of the policy decision-making process.

## Available Environments

The library currently supports policies for the following environments OCAtari, Classic Control and Mujoco.