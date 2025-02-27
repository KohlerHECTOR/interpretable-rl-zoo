def play(x):
    if x[1] <= -0.3075701892375946:
        if x[1] <= -0.6354488134384155:
            return 0
        else:
            if x[0] <= -0.9564911723136902:
                if x[1] <= -0.5357891321182251:
                    if x[0] <= -1.3625571727752686:
                        if x[1] <= -0.6193246841430664:
                            if x[0] <= -1.481126606464386:
                                return 2
                            else:
                                return 0
                        else:
                            return 2
                    else:
                        if x[0] <= -1.1003714799880981:
                            if x[1] <= -0.5914889574050903:
                                return 0
                            else:
                                return 2
                        else:
                            return 0
                else:
                    return 2
            else:
                return 0
    else:
        if x[1] <= -0.07508499175310135:
            if x[0] <= 0.32688190042972565:
                if x[0] <= 0.056232258677482605:
                    if x[0] <= 0.012357823085039854:
                        return 2
                    else:
                        if x[1] <= -0.25150491297245026:
                            return 0
                        else:
                            return 2
                else:
                    if x[1] <= -0.11380346119403839:
                        if x[1] <= -0.12539220601320267:
                            return 0
                        else:
                            if x[0] <= 0.1851518712937832:
                                return 2
                            else:
                                return 0
                    else:
                        return 2
            else:
                if x[1] <= -0.09758877009153366:
                    return 0
                else:
                    if x[0] <= 0.3800569474697113:
                        return 2
                    else:
                        return 0
        else:
            if x[0] <= 1.7818742394447327:
                if x[1] <= -0.007892473135143518:
                    if x[0] <= 0.45815926790237427:
                        return 2
                    else:
                        if x[1] <= -0.037902483716607094:
                            return 0
                        else:
                            if x[0] <= 0.5579420328140259:
                                return 2
                            else:
                                if x[0] <= 0.625333696603775:
                                    if x[0] <= 0.5922213494777679:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 0
                else:
                    return 2
            else:
                if x[1] <= 0.2483629733324051:
                    if x[0] <= 1.8031360507011414:
                        if x[0] <= 1.7904897332191467:
                            return 0
                        else:
                            return 2
                    else:
                        return 0
                else:
                    if x[1] <= 0.26404741406440735:
                        if x[0] <= 1.8866532444953918:
                            return 2
                        else:
                            return 0
                    else:
                        return 2


metadata =  {"algorithm": "PPO", "env_name": "MountainCar-v0"}
