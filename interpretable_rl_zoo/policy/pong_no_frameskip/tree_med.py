def play(x):
    if x[11] <= -4.5:
        if x[2] <= 129.5:
            return 4
        else:
            if x[5] <= 144.0:
                return 3
            else:
                if x[2] <= 134.5:
                    return 1
                else:
                    return 1
    else:
        if x[3] <= 166.5:
            if x[5] <= 152.0:
                if x[3] <= 112.5:
                    if x[3] <= 80.5:
                        if x[3] <= 67.5:
                            if x[5] <= 17.0:
                                return 5
                            else:
                                if x[1] <= 38.0:
                                    return 3
                                else:
                                    return 2
                        else:
                            return 5
                    else:
                        if x[2] <= 112.5:
                            return 4
                        else:
                            return 3
                else:
                    if x[2] <= 139.5:
                        return 5
                    else:
                        return 4
            else:
                if x[5] <= 162.0:
                    return 3
                else:
                    return 5
        else:
            if x[2] <= 117.5:
                return 5
            else:
                return 4


metadata =  {"algorithm": "DQN", "env_name": "PongNoFrameskip-v4"}
