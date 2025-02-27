def play(x):
    if x[0] <= 74.5:
        if x[3] <= 169.5:
            if x[0] <= 40.0:
                return 1
            else:
                return 1
        else:
            if x[2] <= 70.5:
                if x[0] <= 37.5:
                    return 1
                else:
                    return 3
            else:
                return 2
    else:
        if x[2] <= 114.5:
            if x[2] <= 37.5:
                return 3
            else:
                return 3
        else:
            return 2


metadata =  {"algorithm": "DQN", "env_name": "BreakoutNoFrameskip-v4"}
