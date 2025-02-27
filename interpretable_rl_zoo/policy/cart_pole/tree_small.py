def play(x):
    if x[3] <= 0.008984499610960484:
        if x[0] <= 0.12886057049036026:
            if x[2] <= 0.02369958534836769:
                if x[3] <= -0.05572644621133804:
                    return 0
                else:
                    if x[0] <= -0.050685254856944084:
                        return 0
                    else:
                        return 1
            else:
                return 1
        else:
            return 1
    else:
        if x[2] <= -0.03167944587767124:
            return 0
        else:
            if x[0] <= -0.06308601796627045:
                return 1
            else:
                return 1


metadata =  {"algorithm": "PPO", "env_name": "CartPole-v1"}
