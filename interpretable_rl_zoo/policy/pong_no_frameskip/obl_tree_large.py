def play(x):
    if (x[3] - x[15]) <= 163.5:
        if (x[11] - x[12]) <= -15.5:
            if (x[0] - x[3]) <= 25.5:
                if (x[3] - x[8]) <= 110.5:
                    if (x[2] - x[5]) <= -6.0:
                        return 1
                    else:
                        return 4
                else:
                    if (x[2] - x[11]) <= 154.5:
                        if (x[3] - x[12]) <= 153.5:
                            return 0
                        else:
                            return 5
                    else:
                        return 1
            else:
                if (x[2] - x[5]) <= 58.5:
                    if (x[5] - x[12]) <= 85.5:
                        if (x[3] - x[19]) <= 79.5:
                            return 4
                        else:
                            return 4
                    else:
                        return 4
                else:
                    return 3
        else:
            if (x[2] - x[3]) <= 59.5:
                if (x[1] - x[2]) <= -79.5:
                    if (x[3] - x[12]) <= 77.5:
                        return 5
                    else:
                        return 5
                else:
                    if (x[3] - x[14]) <= 122.5:
                        if (x[12] - x[13]) <= 5.5:
                            if (x[5] - x[15]) <= 17.0:
                                return 5
                            else:
                                if (x[5] - x[15]) <= 150.0:
                                    if (x[3] - x[15]) <= 20.5:
                                        return 2
                                    else:
                                        return 3
                                else:
                                    return 3
                        else:
                            if (x[1] - x[2]) <= -67.5:
                                return 4
                            else:
                                return 4
                    else:
                        if (x[1] - x[5]) <= 27.5:
                            if (x[2] - x[12]) <= 135.5:
                                if (x[2] - x[5]) <= -36.5:
                                    return 5
                                else:
                                    return 5
                            else:
                                return 4
                        else:
                            if (x[5] - x[19]) <= 154.0:
                                if (x[5] - x[15]) <= 142.0:
                                    if (x[2] - x[19]) <= 134.5:
                                        return 5
                                    else:
                                        return 4
                                else:
                                    return 1
                            else:
                                return 3
            else:
                if (x[1] - x[2]) <= -80.5:
                    if (x[2] - x[16]) <= 142.5:
                        if (x[1] - x[3]) <= -20.5:
                            return 5
                        else:
                            return 2
                    else:
                        return 0
                else:
                    return 2
    else:
        if (x[2] - x[13]) <= 125.5:
            return 5
        else:
            if (x[4] - x[15]) <= 13.0:
                return 4
            else:
                if (x[1] - x[2]) <= 34.5:
                    return 2
                else:
                    return 4


metadata =  {"algorithm": "DQN", "env_name": "PongNoFrameskip-v4"}
