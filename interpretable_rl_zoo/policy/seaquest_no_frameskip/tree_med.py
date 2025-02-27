def play(x):
    if x[1] <= 86.5:
        if x[0] <= 10.5:
            if x[72] <= 29.0:
                return 13
            else:
                return 6
        else:
            if x[84] <= 95.0:
                if x[0] <= 108.5:
                    if x[1] <= 46.5:
                        if x[88] <= 58.5:
                            return 6
                        else:
                            return 9
                    else:
                        return 9
                else:
                    if x[58] <= 80.5:
                        return 9
                    else:
                        return 4
            else:
                return 17
    else:
        if x[108] <= 0.5:
            if x[14] <= 97.5:
                if x[0] <= 37.5:
                    if x[1] <= 96.5:
                        return 16
                    else:
                        return 14
                else:
                    return 9
            else:
                if x[52] <= 110.5:
                    return 14
                else:
                    return 15
        else:
            if x[1] <= 104.5:
                return 15
            else:
                if x[91] <= -3.5:
                    return 6
                else:
                    return 14


metadata =  {"algorithm": "DQN", "env_name": "SeaquestNoFrameskip-v4"}
