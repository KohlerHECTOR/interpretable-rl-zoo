def play(x):
    if x[1] <= -0.07881922647356987:
        if x[2] <= 5.6460912227630615:
            if x[1] <= -0.19592135399580002:
                if x[0] <= -0.5395686328411102:
                    if x[2] <= -0.24940887093544006:
                        if x[2] <= -4.651739597320557:
                            return [0.6069635766436461]
                        else:
                            return [-1.2555301070230844]
                    else:
                        return [1.958083555548668]
                else:
                    return [1.753728437283246]
            else:
                return [0.6440276008068341]
        else:
            return [-1.7984154333037063]
    else:
        if x[1] <= 0.5690014958381653:
            if x[2] <= -0.11497817561030388:
                if x[0] <= 0.9955593347549438:
                    if x[2] <= -0.6634158492088318:
                        if x[0] <= -9.357929229736328e-06:
                            return [-1.2878658955020053]
                        else:
                            return [0.21511633802143207]
                    else:
                        return [-1.4655261262060038]
                else:
                    return [0.6249301743749929]
            else:
                if x[0] <= 1.475214958190918e-05:
                    if x[2] <= 5.146914958953857:
                        return [1.341596977010016]
                    else:
                        return [-1.0146141868817393]
                else:
                    if x[1] <= -0.018964781425893307:
                        return [-0.615664884582432]
                    else:
                        return [-1.8457857586924866]
        else:
            if x[2] <= -6.205329179763794:
                return [1.670731603215537]
            else:
                return [-1.759567343697718]


metadata =  {"algorithm": "PPO", "env_name": "Pendulum-v1"}
