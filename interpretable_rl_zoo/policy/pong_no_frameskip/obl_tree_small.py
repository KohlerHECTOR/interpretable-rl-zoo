def play(x):
    if x[3] <= 78.5:
        if (x[3] - x[9]) <= 65.5:
            return 2
        else:
            return 5
    else:
        if (x[3] - x[6]) <= -3.5:
            return 4
        else:
            if (x[2] - x[13]) <= 127.5:
                if (x[2] - x[18]) <= 118.5:
                    if (x[2] - x[16]) <= 111.5:
                        return 5
                    else:
                        return 1
                else:
                    return 3
            else:
                if (x[9] - x[11]) <= 2.5:
                    return 4
                else:
                    return 1


metadata =  {"algorithm": "DQN", "env_name": "PongNoFrameskip-v4"}
