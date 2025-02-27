def play(x):
    if (x[4] - x[5]) <= -0.008268624544143677:
        if (x[1] - x[4]) <= -0.853657454252243:
            if x[5] <= 0.4100418835878372:
                return 0
            else:
                if x[5] <= 0.7913704216480255:
                    return 1
                else:
                    return 2
        else:
            return 2
    else:
        if (x[3] - x[5]) <= -0.9228176474571228:
            return 2
        else:
            if (x[1] - x[2]) <= 2.5277034044265747:
                return 0
            else:
                if x[5] <= -0.6809554398059845:
                    return 0
                else:
                    return 2


metadata =  {"algorithm": "PPO", "env_name": "Acrobot-v1"}
