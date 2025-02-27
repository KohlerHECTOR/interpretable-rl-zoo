def play(x):
    if x[0] <= 90.5:
        if x[76] <= 22.5:
            if x[67] <= 108.0:
                if x[82] <= 83.5:
                    if x[76] <= 11.0:
                        if x[39] <= 54.0:
                            if x[13] <= 71.0:
                                return 3
                            else:
                                return 5
                        else:
                            if x[33] <= 74.0:
                                return 2
                            else:
                                return 5
                    else:
                        return 5
                else:
                    if x[17] <= 56.0:
                        if x[0] <= 77.5:
                            if x[0] <= 65.5:
                                return 2
                            else:
                                return 2
                        else:
                            return 2
                    else:
                        return 3
            else:
                return 0
        else:
            if x[58] <= 76.5:
                if x[0] <= 45.0:
                    return 4
                else:
                    return 1
            else:
                return 5
    else:
        if x[39] <= 64.0:
            if x[19] <= 36.0:
                return 5
            else:
                return 5
        else:
            return 5


metadata =  {"algorithm": "DQN", "env_name": "SpaceInvadersNoFrameskip-v4"}
