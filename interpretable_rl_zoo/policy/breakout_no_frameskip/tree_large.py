def play(x):
    if x[0] <= 75.5:
        if x[226] <= -8.0:
            if x[0] <= 43.0:
                if x[2] <= 14.5:
                    return 1
                else:
                    if x[3] <= 81.5:
                        return 3
                    else:
                        return 1
            else:
                if x[2] <= 60.5:
                    return 3
                else:
                    return 2
        else:
            if x[34] <= 64.0:
                if x[3] <= 165.5:
                    if x[226] <= 1.5:
                        if x[0] <= 22.5:
                            if x[229] <= 3.5:
                                return 1
                            else:
                                return 2
                        else:
                            if x[3] <= 91.5:
                                if x[0] <= 44.5:
                                    return 2
                                else:
                                    return 3
                            else:
                                if x[229] <= 7.0:
                                    if x[2] <= 103.5:
                                        return 1
                                    else:
                                        return 1
                                else:
                                    return 3
                    else:
                        if x[226] <= 9.5:
                            return 1
                        else:
                            return 1
                else:
                    if x[226] <= -2.5:
                        return 1
                    else:
                        if x[2] <= 69.5:
                            if x[0] <= 32.0:
                                return 2
                            else:
                                if x[3] <= 189.5:
                                    return 3
                                else:
                                    return 1
                        else:
                            if x[3] <= 191.5:
                                return 2
                            else:
                                if x[0] <= 48.0:
                                    return 1
                                else:
                                    return 3
            else:
                if x[3] <= 145.0:
                    return 3
                else:
                    if x[3] <= 165.5:
                        if x[3] <= 151.5:
                            return 1
                        else:
                            return 0
                    else:
                        if x[2] <= 82.0:
                            return 3
                        else:
                            return 1
    else:
        if x[2] <= 109.5:
            if x[229] <= -3.5:
                return 1
            else:
                return 3
        else:
            if x[3] <= 175.5:
                return 1
            else:
                if x[0] <= 111.5:
                    if x[226] <= -16.5:
                        return 3
                    else:
                        return 2
                else:
                    return 3


metadata =  {"algorithm": "DQN", "env_name": "BreakoutNoFrameskip-v4"}
