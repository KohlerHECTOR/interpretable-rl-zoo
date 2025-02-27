def play(x):
    if x[4] <= -0.010626565665006638:
        if x[3] <= -0.24583563953638077:
            if x[1] <= 1.8370266556739807:
                return 2
            else:
                return 1
        else:
            if x[4] <= -0.12364080920815468:
                return 1
            else:
                if x[0] <= -0.19263038784265518:
                    return 3
                else:
                    if x[1] <= 0.6607346534729004:
                        if x[3] <= -0.14827535301446915:
                            return 2
                        else:
                            return 1
                    else:
                        return 1
    else:
        if x[2] <= -0.012047071941196918:
            if x[5] <= -0.07918135076761246:
                return 2
            else:
                return 3
        else:
            if x[5] <= 0.04499227926135063:
                if x[3] <= -0.21972554177045822:
                    return 2
                else:
                    if x[1] <= 0.45513951778411865:
                        if x[3] <= -0.13370659202337265:
                            return 2
                        else:
                            return 0
                    else:
                        return 1
            else:
                if x[3] <= -0.2853945791721344:
                    return 3
                else:
                    if x[2] <= 0.40111038088798523:
                        return 3
                    else:
                        return 1


metadata =  {"algorithm": "PPO", "env_name": "LunarLander-v2"}
