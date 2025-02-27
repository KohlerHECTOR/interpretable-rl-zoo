def play(x):
    if (x[1] - x[110]) <= 92.5:
        if (x[0] - x[71]) <= -67.5:
            if (x[0] - x[18]) <= 30.5:
                return 16
            else:
                if (x[88] - x[89]) <= -111.5:
                    return 6
                else:
                    return 9
        else:
            if (x[0] - x[19]) <= 37.5:
                return 13
            else:
                return 4
    else:
        if (x[18] - x[140]) <= 78.5:
            if (x[27] - x[88]) <= -110.5:
                return 14
            else:
                return 15
        else:
            return 14


metadata =  {"algorithm": "DQN", "env_name": "SeaquestNoFrameskip-v4"}
