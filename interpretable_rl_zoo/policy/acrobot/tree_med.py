def play(x):
    if x[4] <= -0.008773391135036945:
        if x[5] <= -0.585877537727356:
            return 0
        else:
            if x[1] <= -1.4412310719490051:
                if x[5] <= 0.7834351658821106:
                    if x[5] <= 0.4830177128314972:
                        return 0
                    else:
                        return 1
                else:
                    return 2
            else:
                if x[4] <= -0.04802370257675648:
                    return 2
                else:
                    if x[1] <= -0.00615868135355413:
                        if x[5] <= 0.0922635868191719:
                            return 0
                        else:
                            return 2
                    else:
                        return 2
    else:
        if x[5] <= 0.555562824010849:
            if x[1] <= 1.448271095752716:
                if x[4] <= 0.0375088881701231:
                    if x[1] <= -0.0019042392959818244:
                        return 0
                    else:
                        if x[5] <= -0.10946477577090263:
                            return 0
                        else:
                            return 2
                else:
                    return 0
            else:
                if x[5] <= -0.6760993003845215:
                    return 0
                else:
                    return 2
        else:
            if x[1] <= -1.4634835124015808:
                return 1
            else:
                return 2


metadata =  {"algorithm": "PPO", "env_name": "Acrobot-v1"}
