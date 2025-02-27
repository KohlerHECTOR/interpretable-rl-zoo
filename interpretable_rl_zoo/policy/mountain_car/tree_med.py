def play(x):
    if x[1] <= -0.3119630515575409:
        if x[1] <= -0.6269589066505432:
            return 0
        else:
            if x[0] <= -0.9955593049526215:
                if x[1] <= -0.5344153344631195:
                    if x[0] <= -1.0988650918006897:
                        return 2
                    else:
                        return 0
                else:
                    return 2
            else:
                return 0
    else:
        if x[1] <= -0.1128132976591587:
            if x[0] <= 0.26990067958831787:
                if x[0] <= 0.012178616132587194:
                    return 2
                else:
                    if x[1] <= -0.24635464698076248:
                        return 0
                    else:
                        return 2
            else:
                return 0
        else:
            if x[1] <= -0.020284288562834263:
                if x[0] <= 0.438308522105217:
                    if x[0] <= 0.33850015699863434:
                        return 2
                    else:
                        if x[1] <= -0.08471766486763954:
                            return 0
                        else:
                            return 2
                else:
                    if x[0] <= 0.5327072739601135:
                        if x[1] <= -0.05349183268845081:
                            return 0
                        else:
                            return 2
                    else:
                        return 0
            else:
                return 2


metadata =  {"algorithm": "PPO", "env_name": "MountainCar-v0"}
