def play(x):
    if x[3] <= 168.5:
        if x[0] <= 110.5:
            if x[0] <= 16.0:
                if x[229] <= 3.5:
                    return 1
                else:
                    return 2
            else:
                if x[3] <= 94.5:
                    return 1
                else:
                    if x[229] <= 13.5:
                        return 1
                    else:
                        return 2
        else:
            if x[2] <= 109.5:
                return 3
            else:
                return 1
    else:
        if x[0] <= 61.5:
            if x[3] <= 189.5:
                if x[2] <= 37.5:
                    return 3
                else:
                    if x[2] <= 120.5:
                        return 2
                    else:
                        return 1
            else:
                return 1
        else:
            if x[2] <= 98.5:
                if x[0] <= 81.5:
                    if x[2] <= 77.5:
                        return 3
                    else:
                        return 2
                else:
                    return 3
            else:
                if x[0] <= 110.5:
                    return 2
                else:
                    return 3


metadata =  {"algorithm": "DQN", "env_name": "BreakoutNoFrameskip-v4"}
