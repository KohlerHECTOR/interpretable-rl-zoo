def play(x):
    if x[1] <= -0.30858099460601807:
        if (x[0] - x[1]) <= -0.8528725206851959:
            if x[1] <= -0.6583458185195923:
                return 0
            else:
                return 2
        else:
            if (x[0] - x[1]) <= -0.45516054332256317:
                if x[1] <= -0.6071302592754364:
                    return 0
                else:
                    if (x[0] - x[1]) <= -0.5111161172389984:
                        return 2
                    else:
                        return 0
            else:
                return 0
    else:
        if x[1] <= -0.1116955392062664:
            if (x[0] - x[1]) <= 0.2908623218536377:
                return 2
            else:
                if (x[0] - x[1]) <= 0.3803528845310211:
                    if x[1] <= -0.19842781126499176:
                        return 0
                    else:
                        return 2
                else:
                    return 0
        else:
            if (x[0] - x[1]) <= 1.901855230331421:
                if (x[0] - x[1]) <= 0.44891272485256195:
                    return 2
                else:
                    if x[1] <= -0.02014293149113655:
                        if (x[0] - x[1]) <= 0.5529561340808868:
                            if x[1] <= -0.07615584507584572:
                                return 0
                            else:
                                return 2
                        else:
                            return 0
                    else:
                        return 2
            else:
                return 0


metadata =  {"algorithm": "PPO", "env_name": "MountainCar-v0"}
