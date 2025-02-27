def play(x):
    if x[4] <= -0.009455950930714607:
        if x[5] <= -0.5500974357128143:
            return 0
        else:
            if x[1] <= -1.4020549654960632:
                if x[5] <= 0.7788945138454437:
                    return 0
                else:
                    return 2
            else:
                return 2
    else:
        if x[5] <= 0.5311795771121979:
            if x[1] <= 1.4040064811706543:
                return 0
            else:
                if x[5] <= -0.6188086867332458:
                    return 0
                else:
                    return 2
        else:
            return 2


metadata =  {"algorithm": "PPO", "env_name": "Acrobot-v1"}
