def play(x):
    if x[1] <= -0.30737216770648956:
        if (x[0] - x[1]) <= -0.9218730032444:
            if x[1] <= -0.6594826877117157:
                if (x[0] - x[1]) <= -1.0598204731941223:
                    return 2
                else:
                    return 0
            else:
                if x[1] <= -0.6539997756481171:
                    if (x[0] - x[1]) <= -0.9800148606300354:
                        return 2
                    else:
                        return 0
                else:
                    return 2
        else:
            if (x[0] - x[1]) <= -0.4486207067966461:
                if x[1] <= -0.6325241923332214:
                    if x[1] <= -0.6390374898910522:
                        return 0
                    else:
                        if (x[0] - x[1]) <= -0.8556876480579376:
                            return 2
                        else:
                            return 0
                else:
                    if x[1] <= -0.5336020588874817:
                        if (x[0] - x[1]) <= -0.7664740681648254:
                            if x[1] <= -0.618789941072464:
                                if x[0] <= -1.4723984003067017:
                                    return 2
                                else:
                                    return 0
                            else:
                                if x[1] <= -0.6145754456520081:
                                    if x[1] <= -0.6152476668357849:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 2
                        else:
                            if x[1] <= -0.5426201820373535:
                                return 0
                            else:
                                if (x[0] - x[1]) <= -0.5258868336677551:
                                    return 2
                                else:
                                    return 0
                    else:
                        return 2
            else:
                return 0
    else:
        if (x[0] - x[1]) <= 1.8480615615844727:
            if (x[0] - x[1]) <= 0.4684984087944031:
                if x[1] <= -0.2595085948705673:
                    if (x[0] - x[1]) <= 0.27080048620700836:
                        return 2
                    else:
                        return 0
                else:
                    if (x[0] - x[1]) <= 0.44724932312965393:
                        if (x[0] - x[1]) <= 0.4259766489267349:
                            return 2
                        else:
                            if x[1] <= 0.2926838956773281:
                                return 0
                            else:
                                return 2
                    else:
                        if x[0] <= 0.35580310225486755:
                            return 0
                        else:
                            return 2
            else:
                if x[1] <= -0.021842588670551777:
                    if (x[0] - x[1]) <= 0.556540846824646:
                        if x[1] <= -0.07526173070073128:
                            return 0
                        else:
                            if x[1] <= -0.05151655338704586:
                                if x[0] <= 0.4464958757162094:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 2
                    else:
                        return 0
                else:
                    if x[1] <= 0.26594017446041107:
                        if (x[0] - x[1]) <= 1.555580973625183:
                            if (x[0] - x[1]) <= 0.6645598709583282:
                                return 2
                            else:
                                if x[1] <= 0.22654695808887482:
                                    return 0
                                else:
                                    return 2
                        else:
                            if x[1] <= 0.2496628388762474:
                                if x[1] <= 0.24797870963811874:
                                    return 0
                                else:
                                    if x[0] <= 1.878999650478363:
                                        return 2
                                    else:
                                        return 0
                            else:
                                if (x[0] - x[1]) <= 1.654531717300415:
                                    return 2
                                else:
                                    return 0
                    else:
                        if (x[0] - x[1]) <= 1.7779268026351929:
                            if x[1] <= 0.27013008296489716:
                                if x[0] <= 1.9889426827430725:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 2
                        else:
                            if x[1] <= 0.2948560416698456:
                                if x[1] <= 0.286655068397522:
                                    return 0
                                else:
                                    if x[1] <= 0.28900866210460663:
                                        return 2
                                    else:
                                        return 0
                            else:
                                return 2
        else:
            if x[1] <= 0.2956182658672333:
                return 0
            else:
                return 2


metadata =  {"algorithm": "PPO", "env_name": "MountainCar-v0"}
