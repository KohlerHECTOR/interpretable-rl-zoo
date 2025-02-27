def play(x):
    if (x[0] - x[36]) <= -43.5:
        if (x[40] - x[48]) <= -98.5:
            if (x[28] - x[79]) <= -126.0:
                return 0
            else:
                return 2
        else:
            if (x[8] - x[186]) <= 12.5:
                if (x[73] - x[92]) <= 44.0:
                    return 5
                else:
                    return 3
            else:
                if (x[42] - x[88]) <= 40.5:
                    return 4
                else:
                    return 5
    else:
        if (x[25] - x[42]) <= -20.5:
            return 5
        else:
            return 5


metadata =  {"algorithm": "DQN", "env_name": "SpaceInvadersNoFrameskip-v4"}
