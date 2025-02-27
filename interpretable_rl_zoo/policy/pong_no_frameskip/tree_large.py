def play(x):
    if x[11] <= -7.5:
        if x[2] <= 129.5:
            if x[5] <= 90.0:
                if x[3] <= 77.5:
                    return 5
                else:
                    return 4
            else:
                if x[12] <= -1.0:
                    return 5
                else:
                    return 2
        else:
            if x[2] <= 137.5:
                if x[2] <= 134.5:
                    if x[1] <= 138.0:
                        return 0
                    else:
                        return 1
                else:
                    return 1
            else:
                return 4
    else:
        if x[3] <= 165.5:
            if x[3] <= 63.5:
                if x[2] <= 142.5:
                    if x[5] <= 17.0:
                        return 3
                    else:
                        if x[1] <= 39.5:
                            return 3
                        else:
                            return 2
                else:
                    return 4
            else:
                if x[3] <= 78.5:
                    if x[11] <= 5.5:
                        if x[2] <= 108.5:
                            return 2
                        else:
                            return 5
                    else:
                        return 2
                else:
                    if x[3] <= 113.5:
                        if x[2] <= 113.5:
                            if x[2] <= 79.0:
                                return 3
                            else:
                                return 4
                        else:
                            return 3
                    else:
                        if x[3] <= 153.5:
                            if x[5] <= 146.0:
                                if x[12] <= 43.5:
                                    if x[2] <= 139.5:
                                        if x[12] <= 3.0:
                                            return 1
                                        else:
                                            if x[3] <= 141.5:
                                                if x[3] <= 122.5:
                                                    return 3
                                                else:
                                                    return 5
                                            else:
                                                return 3
                                    else:
                                        return 4
                                else:
                                    return 1
                            else:
                                return 1
                        else:
                            if x[2] <= 127.5:
                                return 3
                            else:
                                return 5
        else:
            if x[2] <= 117.5:
                return 5
            else:
                if x[5] <= 166.0:
                    return 5
                else:
                    if x[11] <= -4.5:
                        if x[5] <= 172.0:
                            return 4
                        else:
                            return 2
                    else:
                        return 4


metadata =  {"algorithm": "DQN", "env_name": "PongNoFrameskip-v4"}
