def play(x):
    if x[87] <= 126.0:
        if x[0] <= 88.5:
            if x[68] <= 67.5:
                return 5
            else:
                if x[86] <= 124.5:
                    return 2
                else:
                    return 5
        else:
            return 5
    else:
        if x[8] <= 43.5:
            if x[9] <= 20.5:
                if x[92] <= 42.0:
                    return 3
                else:
                    return 5
            else:
                return 4
        else:
            return 0


metadata =  {"algorithm": "DQN", "env_name": "SpaceInvadersNoFrameskip-v4"}
