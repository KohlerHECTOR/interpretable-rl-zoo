def play(x):
    if x[3] <= 0.021366069093346596:
        if x[3] <= -0.05325014889240265:
            if x[2] <= 0.059502387419342995:
                if x[0] <= 0.04162650741636753:
                    if x[2] <= 0.010231362655758858:
                        return 0
                    else:
                        if x[3] <= -0.20248060673475266:
                            return 0
                        else:
                            if x[1] <= 0.044826021417975426:
                                return 0
                            else:
                                return 1
                else:
                    if x[3] <= -0.1944798082113266:
                        if x[0] <= 0.4791361838579178:
                            return 0
                        else:
                            return 1
                    else:
                        if x[1] <= 0.0407438687980175:
                            return 0
                        else:
                            return 1
            else:
                return 1
        else:
            if x[1] <= -0.009296752512454987:
                if x[0] <= -0.09074533730745316:
                    return 0
                else:
                    if x[2] <= 0.0003536575968610123:
                        return 0
                    else:
                        return 1
            else:
                if x[2] <= 0.001409570628311485:
                    if x[0] <= -0.009710719808936119:
                        if x[3] <= -0.015326005406677723:
                            return 0
                        else:
                            if x[0] <= -0.041868798434734344:
                                return 0
                            else:
                                if x[2] <= -0.009492266457527876:
                                    return 0
                                else:
                                    return 1
                    else:
                        if x[2] <= -0.013486998155713081:
                            return 0
                        else:
                            return 1
                else:
                    if x[0] <= -0.045312490314245224:
                        if x[3] <= -0.01258367532864213:
                            return 0
                        else:
                            return 1
                    else:
                        return 1
    else:
        if x[0] <= -0.38191601634025574:
            if x[2] <= 0.05570458807051182:
                return 0
            else:
                return 1
        else:
            if x[2] <= -0.038517555221915245:
                return 0
            else:
                if x[3] <= 0.15839312970638275:
                    if x[1] <= -0.13616106659173965:
                        if x[3] <= 0.12044882401823997:
                            return 0
                        else:
                            return 1
                    else:
                        if x[2] <= -0.00043464508780743927:
                            if x[0] <= -0.0698426142334938:
                                return 1
                            else:
                                return 1
                        else:
                            return 1
                else:
                    if x[1] <= -0.34409742057323456:
                        if x[3] <= 0.2992682009935379:
                            return 0
                        else:
                            return 1
                    else:
                        return 1


metadata =  {"algorithm": "PPO", "env_name": "CartPole-v1"}
