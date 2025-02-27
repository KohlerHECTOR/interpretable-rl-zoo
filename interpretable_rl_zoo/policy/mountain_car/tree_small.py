def play(x):
    if x[1] <= -0.25965142250061035:
        if x[1] <= -0.637761116027832:
            return 0
        else:
            if x[0] <= -1.0020567178726196:
                return 2
            else:
                return 0
    else:
        if x[1] <= -0.050793273374438286:
            if x[0] <= 0.29793865978717804:
                if x[0] <= 0.045278776437044144:
                    return 2
                else:
                    if x[1] <= -0.21555758267641068:
                        return 0
                    else:
                        return 2
            else:
                return 0
        else:
            return 2


metadata =  {"algorithm": "PPO", "env_name": "MountainCar-v0"}
