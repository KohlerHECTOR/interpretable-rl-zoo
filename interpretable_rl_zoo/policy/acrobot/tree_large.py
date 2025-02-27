def play(x):
    if x[4] <= -0.011253893375396729:
        if x[5] <= -0.6143328249454498:
            if x[5] <= -0.695595771074295:
                return 0
            else:
                if x[1] <= 1.4363198280334473:
                    return 0
                else:
                    if x[3] <= -0.7493839859962463:
                        return 0
                    else:
                        return 2
        else:
            if x[1] <= -1.447817325592041:
                if x[5] <= 0.7872257232666016:
                    if x[5] <= 0.4840136617422104:
                        return 0
                    else:
                        if x[3] <= -0.572708860039711:
                            return 2
                        else:
                            return 1
                else:
                    return 2
            else:
                if x[4] <= -0.04920949600636959:
                    if x[1] <= -1.110023856163025:
                        if x[5] <= 0.4150726944208145:
                            if x[5] <= -0.10836420953273773:
                                return 0
                            else:
                                return 1
                        else:
                            return 2
                    else:
                        if x[4] <= -0.07752586901187897:
                            return 2
                        else:
                            if x[3] <= 0.5908400118350983:
                                return 2
                            else:
                                if x[5] <= 0.0864633098244667:
                                    return 0
                                else:
                                    return 2
                else:
                    if x[1] <= 0.014176907949149609:
                        if x[5] <= 0.08948466554284096:
                            return 0
                        else:
                            return 2
                    else:
                        return 2
    else:
        if x[1] <= 1.4546895623207092:
            if x[5] <= 0.5489105880260468:
                if x[4] <= 0.04349131882190704:
                    if x[1] <= 0.018179889768362045:
                        return 0
                    else:
                        if x[5] <= -0.091826681047678:
                            return 0
                        else:
                            return 2
                else:
                    if x[0] <= -1.7141655683517456:
                        if x[5] <= -0.581133246421814:
                            return 0
                        else:
                            if x[1] <= 0.3074396252632141:
                                return 0
                            else:
                                return 2
                    else:
                        return 0
            else:
                if x[1] <= -1.4727879166603088:
                    if x[5] <= 0.8466291725635529:
                        return 1
                    else:
                        return 2
                else:
                    return 2
        else:
            if x[5] <= -0.6732146739959717:
                if x[2] <= -1.3975512981414795:
                    if x[5] <= -0.7762003839015961:
                        return 0
                    else:
                        return 2
                else:
                    return 0
            else:
                return 2


metadata =  {"algorithm": "PPO", "env_name": "Acrobot-v1"}
