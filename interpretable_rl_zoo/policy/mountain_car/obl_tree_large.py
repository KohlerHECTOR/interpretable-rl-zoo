def play(x):
    if x[1] <= -0.3075243830680847:
        if (x[0] - x[1]) <= -0.9221260249614716:
            if x[1] <= -0.6593068838119507:
                if (x[0] - x[1]) <= -1.0598334074020386:
                    return 2
                else:
                    return 0
            else:
                if x[1] <= -0.6547119319438934:
                    if x[0] <= -1.638469398021698:
                        return 2
                    else:
                        return 0
                else:
                    return 2
        else:
            if (x[0] - x[1]) <= -0.45330025255680084:
                if x[1] <= -0.6188580095767975:
                    if x[1] <= -0.637486457824707:
                        return 0
                    else:
                        if (x[0] - x[1]) <= -0.8463864028453827:
                            return 2
                        else:
                            return 0
                else:
                    if (x[0] - x[1]) <= -0.5093351006507874:
                        if x[1] <= -0.6084507703781128:
                            if x[0] <= -1.369800090789795:
                                return 2
                            else:
                                return 0
                        else:
                            return 2
                    else:
                        if x[0] <= -1.0123249292373657:
                            return 0
                        else:
                            return 2
            else:
                return 0
    else:
        if (x[0] - x[1]) <= 1.9053156971931458:
            if (x[0] - x[1]) <= 0.44797641038894653:
                if x[1] <= -0.2595139592885971:
                    if (x[0] - x[1]) <= 0.27130553126335144:
                        return 2
                    else:
                        return 0
                else:
                    if (x[0] - x[1]) <= 0.42593950033187866:
                        return 2
                    else:
                        return 2
            else:
                if x[1] <= -0.05134881101548672:
                    if (x[0] - x[1]) <= 0.4970805495977402:
                        if x[1] <= -0.07624653726816177:
                            if x[1] <= -0.0948975645005703:
                                return 0
                            else:
                                if x[0] <= 0.38123784959316254:
                                    return 2
                                else:
                                    return 0
                        else:
                            return 2
                    else:
                        return 0
                else:
                    if x[1] <= 0.26451733708381653:
                        if (x[0] - x[1]) <= 0.6529954075813293:
                            if (x[0] - x[1]) <= 0.5900871455669403:
                                return 2
                            else:
                                if x[0] <= 0.5920491218566895:
                                    return 0
                                else:
                                    return 2
                        else:
                            if x[1] <= 0.23637279868125916:
                                return 0
                            else:
                                if (x[0] - x[1]) <= 1.6068230271339417:
                                    return 2
                                else:
                                    return 0
                    else:
                        return 2
        else:
            if x[0] <= 2.257426381111145:
                return 0
            else:
                return 2


metadata =  {"algorithm": "PPO", "env_name": "MountainCar-v0"}
