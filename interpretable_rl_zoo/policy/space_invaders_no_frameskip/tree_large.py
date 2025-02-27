def play(x):
    if x[75] <= 108.0:
        if x[44] <= 60.5:
            if x[78] <= 39.5:
                if x[93] <= 92.5:
                    if x[71] <= 128.0:
                        return 4
                    else:
                        return 5
                else:
                    return 5
            else:
                if x[0] <= 49.0:
                    if x[0] <= 43.0:
                        return 4
                    else:
                        return 1
                else:
                    return 5
        else:
            if x[80] <= 63.5:
                if x[8] <= 40.5:
                    if x[84] <= 99.5:
                        return 5
                    else:
                        return 2
                else:
                    return 5
            else:
                if x[0] <= 79.5:
                    if x[26] <= 115.5:
                        if x[10] <= 15.0:
                            return 3
                        else:
                            return 5
                    else:
                        return 2
                else:
                    if x[84] <= 104.5:
                        return 0
                    else:
                        if x[9] <= 15.5:
                            return 3
                        else:
                            return 5
    else:
        if x[54] <= 54.5:
            if x[84] <= 84.5:
                if x[8] <= 38.5:
                    if x[92] <= 42.0:
                        if x[61] <= 100.0:
                            return 3
                        else:
                            if x[44] <= 19.0:
                                return 2
                            else:
                                return 5
                    else:
                        return 5
                else:
                    return 0
            else:
                if x[0] <= 115.5:
                    if x[80] <= 54.5:
                        if x[42] <= 43.5:
                            if x[0] <= 53.5:
                                return 4
                            else:
                                return 2
                        else:
                            if x[20] <= 30.0:
                                return 5
                            else:
                                if x[56] <= 67.5:
                                    if x[29] <= 64.0:
                                        return 3
                                    else:
                                        return 2
                                else:
                                    return 2
                    else:
                        return 0
                else:
                    return 1
        else:
            if x[25] <= 46.0:
                if x[0] <= 83.0:
                    return 0
                else:
                    if x[0] <= 111.0:
                        return 5
                    else:
                        return 0
            else:
                return 4


metadata =  {"algorithm": "DQN", "env_name": "SpaceInvadersNoFrameskip-v4"}
