def play(x):
    if x[3] <= 0.0011192738311365247:
        if x[2] <= 0.01635880023241043:
            if x[0] <= 0.000635969452559948:
                return 0
            else:
                if x[3] <= -0.07501969113945961:
                    return 0
                else:
                    if x[1] <= 0.003295293776318431:
                        return 0
                    else:
                        return 1
        else:
            if x[3] <= -0.23713937401771545:
                return 0
            else:
                if x[1] <= 0.09679521806538105:
                    if x[0] <= -0.07980456203222275:
                        return 0
                    else:
                        return 1
                else:
                    return 1
    else:
        if x[2] <= -0.06061085686087608:
            return 0
        else:
            if x[3] <= 0.13238979130983353:
                if x[1] <= -0.004899717168882489:
                    if x[0] <= -0.12848718464374542:
                        return 0
                    else:
                        if x[2] <= -0.00039521737198811024:
                            return 0
                        else:
                            return 1
                else:
                    return 1
            else:
                if x[1] <= -0.2906312197446823:
                    if x[3] <= 0.27143557369709015:
                        return 0
                    else:
                        return 1
                else:
                    return 1


metadata =  {"algorithm": "PPO", "env_name": "CartPole-v1"}
