def play(x):
    if x[3] <= -0.14962317049503326:
        if x[2] <= -0.11858590319752693:
            if x[5] <= -0.09734800830483437:
                if x[4] <= 0.16163291037082672:
                    return 2
                else:
                    return 3
            else:
                if x[4] <= 0.0032411912688985467:
                    return 3
                else:
                    return 3
        else:
            if x[4] <= -0.0006721807585563511:
                if x[0] <= 0.022562647238373756:
                    if x[3] <= -0.22536823898553848:
                        return 2
                    else:
                        if x[4] <= -0.12082714959979057:
                            return 1
                        else:
                            if x[5] <= 0.029337490908801556:
                                if x[1] <= 0.6118410527706146:
                                    return 2
                                else:
                                    return 1
                            else:
                                return 3
                else:
                    if x[3] <= -0.2850275933742523:
                        return 2
                    else:
                        if x[2] <= 0.06791849434375763:
                            return 2
                        else:
                            return 1
            else:
                if x[5] <= 0.05413200519979:
                    if x[3] <= -0.25313541293144226:
                        return 2
                    else:
                        if x[1] <= 0.6282618343830109:
                            return 2
                        else:
                            if x[2] <= 0.06405453383922577:
                                return 3
                            else:
                                return 1
                else:
                    if x[2] <= 0.25504057109355927:
                        return 3
                    else:
                        if x[5] <= 0.1417485550045967:
                            return 2
                        else:
                            return 3
    else:
        if x[7] <= 0.5:
            if x[4] <= 0.044108813628554344:
                if x[0] <= 0.11402416229248047:
                    if x[4] <= -0.014611086808145046:
                        return 1
                    else:
                        if x[2] <= -0.061333831399679184:
                            return 3
                        else:
                            if x[1] <= 0.6368044912815094:
                                return 0
                            else:
                                return 1
                else:
                    return 1
            else:
                if x[0] <= 0.055995941162109375:
                    return 3
                else:
                    return 1
        else:
            if x[4] <= -0.08221833407878876:
                if x[0] <= -0.6180185079574585:
                    return 3
                else:
                    return 1
            else:
                if x[4] <= 0.19731788337230682:
                    if x[0] <= -0.2080375701189041:
                        return 3
                    else:
                        if x[3] <= -0.0050530522130429745:
                            return 0
                        else:
                            return 0
                else:
                    return 3


metadata =  {"algorithm": "PPO", "env_name": "LunarLander-v2"}
