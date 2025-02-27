def play(x):
    if (x[4] - x[5]) <= -0.08317610993981361:
        if (x[1] - x[4]) <= -1.1441652178764343:
            if x[5] <= 0.46086034178733826:
                return 0
            else:
                if x[5] <= 0.7903709709644318:
                    return 1
                else:
                    return 2
        else:
            if (x[3] - x[5]) <= 0.5692139267921448:
                return 2
            else:
                if x[1] <= -1.3777899146080017:
                    return 1
                else:
                    if (x[0] - x[5]) <= 0.7416651248931885:
                        return 2
                    else:
                        return 0
    else:
        if (x[3] - x[5]) <= -0.8934332132339478:
            if x[1] <= -0.5816709399223328:
                return 0
            else:
                return 2
        else:
            if (x[1] - x[2]) <= 2.6590781211853027:
                if (x[0] - x[4]) <= 0.8006453216075897:
                    return 0
                else:
                    if (x[0] - x[5]) <= 0.9426824450492859:
                        if (x[1] - x[4]) <= 0.02284792996942997:
                            return 0
                        else:
                            return 2
                    else:
                        return 0
            else:
                if x[5] <= -0.7409898936748505:
                    return 0
                else:
                    if (x[0] - x[5]) <= -0.11740879714488983:
                        return 2
                    else:
                        return 0


metadata =  {"algorithm": "PPO", "env_name": "Acrobot-v1"}
