def play(x):
    if x[1] <= 93.5:
        if x[0] <= 10.5:
            if x[73] <= 89.0:
                return 13
            else:
                return 6
        else:
            if x[18] <= 0.5:
                if x[84] <= 95.0:
                    if x[0] <= 30.5:
                        return 16
                    else:
                        if x[14] <= 11.5:
                            if x[178] <= 0.5:
                                if x[72] <= 29.0:
                                    return 9
                                else:
                                    return 9
                            else:
                                if x[88] <= 58.5:
                                    return 6
                                else:
                                    return 9
                        else:
                            return 9
                else:
                    if x[50] <= 8.5:
                        return 16
                    else:
                        return 0
            else:
                if x[0] <= 53.5:
                    if x[1] <= 87.5:
                        return 8
                    else:
                        return 15
                else:
                    return 4
    else:
        if x[0] <= 34.5:
            if x[18] <= 72.5:
                if x[108] <= 0.5:
                    if x[88] <= 109.5:
                        if x[73] <= 89.0:
                            if x[1] <= 110.5:
                                return 16
                            else:
                                return 10
                        else:
                            if x[69] <= 125.5:
                                return 14
                            else:
                                return 14
                    else:
                        return 14
                else:
                    if x[18] <= 27.5:
                        return 6
                    else:
                        return 14
            else:
                return 14
        else:
            if x[108] <= 0.5:
                if x[88] <= 108.5:
                    if x[1] <= 110.5:
                        if x[14] <= 79.5:
                            return 9
                        else:
                            return 14
                    else:
                        if x[102] <= 0.5:
                            return 11
                        else:
                            return 15
                else:
                    return 12
            else:
                if x[0] <= 101.5:
                    if x[18] <= 73.5:
                        if x[0] <= 49.5:
                            return 6
                        else:
                            return 15
                    else:
                        return 14
                else:
                    if x[8] <= 98.5:
                        if x[99] <= -0.5:
                            return 15
                        else:
                            return 13
                    else:
                        return 7


metadata =  {"algorithm": "DQN", "env_name": "SeaquestNoFrameskip-v4"}
