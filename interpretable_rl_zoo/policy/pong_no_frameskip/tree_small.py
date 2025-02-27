def play(x):
    if x[2] <= 139.5:
        if x[13] <= -1.5:
            if x[3] <= 78.5:
                if x[3] <= 66.5:
                    return 2
                else:
                    return 5
            else:
                if x[5] <= 90.0:
                    return 4
                else:
                    if x[5] <= 98.0:
                        return 2
                    else:
                        return 4
        else:
            if x[2] <= 132.5:
                return 5
            else:
                return 4
    else:
        return 4


metadata =  {"algorithm": "DQN", "env_name": "PongNoFrameskip-v4"}
