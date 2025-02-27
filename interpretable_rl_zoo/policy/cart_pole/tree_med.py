def play(x):
    if x[3] <= -0.004793310770764947:
        if x[2] <= 0.016924629919230938:
            if x[3] <= -0.06728209555149078:
                return 0
            else:
                if x[1] <= 0.024066765792667866:
                    return 0
                else:
                    return 1
        else:
            if x[3] <= -0.19580888748168945:
                if x[1] <= 0.32635271549224854:
                    return 0
                else:
                    if x[3] <= -0.5317357778549194:
                        return 0
                    else:
                        return 1
            else:
                if x[1] <= 0.1360020637512207:
                    return 0
                else:
                    return 1
    else:
        if x[2] <= -0.029967627488076687:
            return 0
        else:
            if x[0] <= -0.10816997289657593:
                if x[3] <= 0.15922857075929642:
                    if x[1] <= -0.03005966078490019:
                        return 0
                    else:
                        return 1
                else:
                    return 1
            else:
                if x[3] <= 0.047838788479566574:
                    if x[1] <= -0.008175039663910866:
                        if x[2] <= -0.0011961024138145149:
                            return 0
                        else:
                            return 1
                    else:
                        return 1
                else:
                    return 1


metadata =  {"algorithm": "PPO", "env_name": "CartPole-v1"}
