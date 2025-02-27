def play(x):
    if (x[0] - x[48]) <= -41.5:
        if (x[8] - x[77]) <= 12.5:
            if (x[68] - x[77]) <= -54.5:
                if (x[67] - x[93]) <= 51.5:
                    return 5
                else:
                    if (x[0] - x[42]) <= 1.5:
                        return 4
                    else:
                        return 1
            else:
                if (x[93] - x[186]) <= 42.0:
                    if (x[28] - x[113]) <= 35.5:
                        return 3
                    else:
                        return 5
                else:
                    return 5
        else:
            if (x[28] - x[47]) <= -39.5:
                if (x[29] - x[43]) <= -72.0:
                    return 0
                else:
                    return 4
            else:
                if (x[68] - x[134]) <= 67.5:
                    return 5
                else:
                    if (x[30] - x[65]) <= 61.5:
                        return 2
                    else:
                        return 5
    else:
        if (x[12] - x[80]) <= -72.5:
            return 5
        else:
            if (x[0] - x[77]) <= 35.0:
                return 5
            else:
                if (x[69] - x[82]) <= 31.5:
                    return 0
                else:
                    if (x[12] - x[42]) <= -38.5:
                        return 3
                    else:
                        return 5


metadata =  {"algorithm": "DQN", "env_name": "SpaceInvadersNoFrameskip-v4"}
