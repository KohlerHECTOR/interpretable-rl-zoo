def play(x):
    if (x[0] - x[1]) <= -0.6382045149803162:
        if (x[0] - x[1]) <= -1.6803735494613647:
            if x[0] <= -0.9972810745239258:
                return [0.9365289653732238]
            else:
                return [0.6937069415973719]
        else:
            return [0.46190309246655575]
    else:
        if (x[0] - x[1]) <= 0.6484068036079407:
            if (x[0] - x[1]) <= 0.13075345009565353:
                if (x[0] - x[1]) <= -0.21018190681934357:
                    return [0.22030196303413027]
                else:
                    return [0.05288615647633802]
            else:
                return [-0.11034526944063773]
        else:
            if (x[0] - x[1]) <= 1.5705665946006775:
                return [-0.3695036706524671]
            else:
                return [-0.6408531232021095]


metadata =  {"algorithm": "PPO", "env_name": "MountainCarContinuous-v0"}
