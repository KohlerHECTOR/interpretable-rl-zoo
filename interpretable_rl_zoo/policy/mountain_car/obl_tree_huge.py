def play(x):
    if x[1] <= -0.3074163794517517:
        if (x[0] - x[1]) <= -0.9219678640365601:
            if x[1] <= -0.6563703417778015:
                if (x[0] - x[1]) <= -1.0598148107528687:
                    return 2
                else:
                    if x[1] <= -0.6592157781124115:
                        return 0
                    else:
                        if (x[0] - x[1]) <= -0.9799541234970093:
                            return 2
                        else:
                            return 0
            else:
                if x[1] <= -0.6540039479732513:
                    if x[0] <= -1.6694156527519226:
                        return 2
                    else:
                        return 0
                else:
                    return 2
        else:
            if (x[0] - x[1]) <= -0.4527849853038788:
                if x[1] <= -0.6164238154888153:
                    if x[1] <= -0.6383844912052155:
                        return 0
                    else:
                        if (x[0] - x[1]) <= -0.8131731152534485:
                            return 2
                        else:
                            return 0
                else:
                    if (x[0] - x[1]) <= -0.5224423706531525:
                        if x[1] <= -0.6086103618144989:
                            if (x[0] - x[1]) <= -0.7579733431339264:
                                return 2
                            else:
                                return 0
                        else:
                            return 2
                    else:
                        if x[1] <= -0.5336156189441681:
                            return 0
                        else:
                            return 2
            else:
                return 0
    else:
        if (x[0] - x[1]) <= 0.4769114553928375:
            if x[1] <= -0.25962936878204346:
                if (x[0] - x[1]) <= 0.27093005180358887:
                    return 2
                else:
                    return 0
            else:
                if (x[0] - x[1]) <= 0.42593978345394135:
                    return 2
                else:
                    if x[0] <= 0.3554236441850662:
                        return 0
                    else:
                        return 2
        else:
            if x[1] <= -0.021765362471342087:
                if (x[0] - x[1]) <= 0.557141125202179:
                    if x[1] <= -0.05177057348191738:
                        if x[1] <= -0.07523468136787415:
                            return 0
                        else:
                            if (x[0] - x[1]) <= 0.5104158520698547:
                                return 2
                            else:
                                return 0
                    else:
                        return 2
                else:
                    return 0
            else:
                if (x[0] - x[1]) <= 1.7544471621513367:
                    if x[1] <= 0.27184295654296875:
                        if (x[0] - x[1]) <= 0.664706826210022:
                            return 2
                        else:
                            if x[1] <= 0.23526756465435028:
                                return 0
                            else:
                                if (x[0] - x[1]) <= 1.6067834496498108:
                                    return 2
                                else:
                                    if x[1] <= 0.2572326958179474:
                                        return 0
                                    else:
                                        if (x[0] - x[1]) <= 1.6989224553108215:
                                            return 2
                                        else:
                                            return 0
                    else:
                        return 2
                else:
                    if x[1] <= 0.2783609628677368:
                        return 0
                    else:
                        if x[1] <= 0.2851317971944809:
                            if (x[0] - x[1]) <= 1.795393466949463:
                                return 2
                            else:
                                return 0
                        else:
                            return 2


metadata =  {"algorithm": "PPO", "env_name": "MountainCar-v0"}
