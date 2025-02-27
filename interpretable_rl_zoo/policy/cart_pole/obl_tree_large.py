def play(x):
    if x[3] <= -0.00822915742173791:
        if x[2] <= 0.035214172676205635:
            if x[0] <= 0.01724973227828741:
                if x[3] <= -0.046547504141926765:
                    if x[2] <= 0.014474221039563417:
                        return 0
                    else:
                        return 0
                else:
                    if x[1] <= 0.0018623649957589805:
                        return 0
                    else:
                        if x[2] <= 0.0009060032898560166:
                            if x[0] <= -0.013400883879512548:
                                return 0
                            else:
                                return 1
                        else:
                            return 1
            else:
                if x[2] <= -0.006440953817218542:
                    if x[0] <= 0.6346697211265564:
                        return 0
                    else:
                        return 1
                else:
                    if x[3] <= -0.1721898466348648:
                        if (x[1] - x[2]) <= 0.31834810972213745:
                            return 0
                        else:
                            return 1
                    else:
                        return 1
        else:
            if x[1] <= 0.32518869638442993:
                return 1
            else:
                if x[3] <= -0.5063401162624359:
                    return 0
                else:
                    return 1
    else:
        if x[0] <= -0.156350277364254:
            if x[2] <= 0.007378519047051668:
                if x[3] <= 0.26360177993774414:
                    return 0
                else:
                    if x[1] <= -0.288831502199173:
                        return 0
                    else:
                        return 1
            else:
                return 1
        else:
            if x[2] <= -0.027684775181114674:
                if x[3] <= 0.18173812329769135:
                    if x[1] <= 0.00023044145200401545:
                        return 0
                    else:
                        return 1
                else:
                    if x[1] <= -0.28651419281959534:
                        if x[3] <= 0.6024559438228607:
                            return 0
                        else:
                            return 1
                    else:
                        return 1
            else:
                if x[3] <= 0.13821692019701004:
                    if x[1] <= -0.1588202640414238:
                        if x[2] <= 0.025640823878347874:
                            return 0
                        else:
                            return 1
                    else:
                        if x[3] <= 0.01933291368186474:
                            if x[1] <= -0.011441274546086788:
                                if x[2] <= 0.0060507869347929955:
                                    return 0
                                else:
                                    return 1
                            else:
                                return 1
                        else:
                            if x[1] <= -0.035119082778692245:
                                if x[2] <= -0.0014468571753241122:
                                    return 1
                                else:
                                    return 1
                            else:
                                return 1
                else:
                    return 1


metadata =  {"algorithm": "PPO", "env_name": "CartPole-v1"}
