def play(x):
    if (x[0] - x[14]) <= 78.5:
        if (x[45] - x[89]) <= 92.0:
            if (x[64] - x[88]) <= -2.0:
                if (x[10] - x[54]) <= -47.5:
                    if (x[92] - x[94]) <= 0.5:
                        if (x[16] - x[186]) <= 37.5:
                            if (x[12] - x[40]) <= 2.5:
                                return 3
                            else:
                                return 3
                        else:
                            return 0
                    else:
                        return 2
                else:
                    if (x[0] - x[40]) <= 20.5:
                        if (x[9] - x[80]) <= 63.5:
                            return 2
                        else:
                            return 4
                    else:
                        if (x[55] - x[86]) <= -31.5:
                            if (x[5] - x[18]) <= 96.5:
                                return 2
                            else:
                                return 2
                        else:
                            if (x[17] - x[80]) <= -29.5:
                                return 0
                            else:
                                return 2
            else:
                if (x[15] - x[78]) <= -39.5:
                    if (x[0] - x[80]) <= -10.5:
                        if (x[0] - x[94]) <= 43.0:
                            return 4
                        else:
                            return 1
                    else:
                        return 5
                else:
                    if (x[37] - x[79]) <= 54.0:
                        if (x[16] - x[110]) <= 27.5:
                            if (x[27] - x[54]) <= -7.5:
                                return 4
                            else:
                                return 5
                        else:
                            if (x[38] - x[53]) <= 24.5:
                                return 3
                            else:
                                return 5
                    else:
                        if (x[0] - x[59]) <= 115.0:
                            if (x[44] - x[88]) <= 74.5:
                                if (x[41] - x[56]) <= 22.5:
                                    if (x[8] - x[87]) <= -103.5:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 4
                            else:
                                if (x[28] - x[89]) <= 46.5:
                                    return 5
                                else:
                                    return 2
                        else:
                            return 0
        else:
            if (x[0] - x[33]) <= -3.5:
                if (x[14] - x[42]) <= -42.5:
                    return 3
                else:
                    return 5
            else:
                return 3
    else:
        if (x[49] - x[55]) <= 82.0:
            if (x[12] - x[54]) <= 63.5:
                if (x[4] - x[70]) <= -21.5:
                    return 3
                else:
                    if (x[17] - x[28]) <= 38.0:
                        return 5
                    else:
                        return 3
            else:
                if (x[44] - x[75]) <= -40.5:
                    return 0
                else:
                    return 5
        else:
            return 3


metadata =  {"algorithm": "DQN", "env_name": "SpaceInvadersNoFrameskip-v4"}
