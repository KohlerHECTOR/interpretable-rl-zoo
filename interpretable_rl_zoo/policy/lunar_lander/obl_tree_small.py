def play(x):
    if (x[3] - x[4]) <= -0.1521359607577324:
        if (x[2] - x[3]) <= 0.048850104212760925:
            return 3
        else:
            if x[5] <= 0.030085919424891472:
                return 2
            else:
                if (x[2] - x[4]) <= 0.06110403873026371:
                    return 3
                else:
                    return 2
    else:
        if (x[0] - x[6]) <= -0.840122252702713:
            return 0
        else:
            if (x[0] - x[4]) <= -0.0069818152114748955:
                return 3
            else:
                if x[3] <= -0.2277597337961197:
                    return 1
                else:
                    return 1


metadata =  {"algorithm": "PPO", "env_name": "LunarLander-v2"}
