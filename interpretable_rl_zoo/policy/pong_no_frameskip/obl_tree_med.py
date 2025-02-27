def play(x):
    if (x[12] - x[15]) <= 8.5:
        if (x[2] - x[7]) <= 139.5:
            if (x[12] - x[13]) <= 5.5:
                if (x[2] - x[7]) <= 130.5:
                    if (x[3] - x[14]) <= 110.5:
                        if (x[5] - x[11]) <= 13.5:
                            return 5
                        else:
                            return 4
                    else:
                        return 5
                else:
                    if (x[3] - x[11]) <= 173.5:
                        return 4
                    else:
                        return 1
            else:
                if (x[1] - x[2]) <= -80.5:
                    if (x[1] - x[3]) <= -28.5:
                        return 5
                    else:
                        return 3
                else:
                    if (x[3] - x[9]) <= 73.5:
                        return 2
                    else:
                        if (x[2] - x[17]) <= 100.5:
                            return 2
                        else:
                            return 4
        else:
            return 4
    else:
        if (x[1] - x[13]) <= 156.5:
            if (x[3] - x[12]) <= 143.0:
                if (x[1] - x[14]) <= 114.5:
                    return 4
                else:
                    return 1
            else:
                if (x[2] - x[11]) <= 150.5:
                    return 0
                else:
                    return 1
        else:
            return 4


metadata =  {"algorithm": "DQN", "env_name": "PongNoFrameskip-v4"}
