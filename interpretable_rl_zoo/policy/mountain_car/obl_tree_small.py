def play(x):
    if x[1] <= -0.2596428543329239:
        if (x[0] - x[1]) <= -0.6719375848770142:
            if x[1] <= -0.62849161028862:
                return 0
            else:
                return 2
        else:
            return 0
    else:
        if x[1] <= -0.051234789192676544:
            if (x[0] - x[1]) <= 0.42595773935317993:
                if (x[0] - x[1]) <= 0.29970216751098633:
                    return 2
                else:
                    if x[1] <= -0.17056898772716522:
                        return 0
                    else:
                        return 2
            else:
                return 0
        else:
            return 2


metadata =  {"algorithm": "PPO", "env_name": "MountainCar-v0"}
