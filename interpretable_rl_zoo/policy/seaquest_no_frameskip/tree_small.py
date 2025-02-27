def play(x):
    if x[1] <= 92.5:
        if x[71] <= 85.0:
            return 13
        else:
            if x[84] <= 95.0:
                if x[88] <= 25.0:
                    return 9
                else:
                    if x[88] <= 58.5:
                        return 6
                    else:
                        return 9
            else:
                return 16
    else:
        if x[52] <= 83.5:
            if x[108] <= 0.5:
                return 14
            else:
                return 15
        else:
            return 14


metadata =  {"algorithm": "DQN", "env_name": "SeaquestNoFrameskip-v4"}
