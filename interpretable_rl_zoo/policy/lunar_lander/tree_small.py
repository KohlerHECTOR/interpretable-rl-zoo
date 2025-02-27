def play(x):
    if x[4] <= -0.018328535370528698:
        if x[3] <= -0.2757493704557419:
            return 2
        else:
            if x[4] <= -0.16925550997257233:
                return 1
            else:
                return 1
    else:
        if x[2] <= -0.0594903789460659:
            if x[5] <= -0.1846178099513054:
                return 2
            else:
                return 3
        else:
            if x[5] <= -0.000974723428953439:
                if x[3] <= -0.2062869668006897:
                    return 2
                else:
                    return 1
            else:
                return 3


metadata =  {"algorithm": "PPO", "env_name": "LunarLander-v2"}
