def play(x):
    if x[4] <= 0.001969692064449191:
        if (x[1] - x[4]) <= -1.0671095848083496:
            if x[5] <= 0.4680086821317673:
                return 0
            else:
                if x[5] <= 0.7938584983348846:
                    if (x[0] - x[2]) <= -1.318514660000801:
                        return 2
                    else:
                        return 1
                else:
                    return 2
        else:
            if x[5] <= -0.5949819087982178:
                if (x[1] - x[2]) <= 3.1392706632614136:
                    return 0
                else:
                    return 2
            else:
                if x[4] <= -0.04864128120243549:
                    if x[1] <= -1.1429429054260254:
                        if x[5] <= 0.40394748747348785:
                            if (x[4] - x[5]) <= -1.3774664402008057:
                                return 1
                            else:
                                return 0
                        else:
                            if x[5] <= 0.7866603136062622:
                                if (x[2] - x[3]) <= -1.8823741674423218:
                                    return 1
                                else:
                                    return 2
                            else:
                                return 2
                    else:
                        return 2
                else:
                    if (x[1] - x[2]) <= -1.1216012239456177:
                        if x[5] <= 0.08891478180885315:
                            return 0
                        else:
                            return 2
                    else:
                        if (x[0] - x[5]) <= 0.9435701668262482:
                            return 2
                        else:
                            return 0
    else:
        if (x[1] - x[4]) <= 1.0279470682144165:
            if x[5] <= 0.5593854784965515:
                if x[4] <= 0.0481183473020792:
                    if (x[1] - x[4]) <= -0.0032095108181238174:
                        return 0
                    else:
                        if (x[0] - x[5]) <= 0.9412053227424622:
                            return 2
                        else:
                            return 0
                else:
                    if (x[3] - x[5]) <= -0.960131049156189:
                        if (x[0] - x[1]) <= -1.3430472016334534:
                            return 2
                        else:
                            return 0
                    else:
                        if (x[1] - x[2]) <= 2.4239472150802612:
                            return 0
                        else:
                            if (x[4] - x[5]) <= 1.378408133983612:
                                if x[5] <= -0.4219355881214142:
                                    return 0
                                else:
                                    return 2
                            else:
                                if (x[0] - x[5]) <= -0.531108021736145:
                                    if x[5] <= -0.5891592800617218:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 0
            else:
                if x[1] <= -1.4643611907958984:
                    if (x[1] - x[5]) <= -2.329257845878601:
                        return 2
                    else:
                        return 1
                else:
                    return 2
        else:
            if x[5] <= -0.7785848677158356:
                return 0
            else:
                return 2


metadata =  {"algorithm": "PPO", "env_name": "Acrobot-v1"}
