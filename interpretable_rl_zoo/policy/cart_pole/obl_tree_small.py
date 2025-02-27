def play(x):
    if x[3] <= -0.014108523726463318:
        if x[0] <= 0.09075838327407837:
            if x[2] <= 0.012263906188309193:
                return 0
            else:
                if x[3] <= -0.23022325336933136:
                    return 0
                else:
                    return 1
        else:
            if x[2] <= -0.031030168756842613:
                return 0
            else:
                return 1
    else:
        if x[3] <= 0.17316725105047226:
            if x[1] <= -0.09493050165474415:
                return 0
            else:
                return 1
        else:
            return 1


metadata =  {"algorithm": "PPO", "env_name": "CartPole-v1"}
