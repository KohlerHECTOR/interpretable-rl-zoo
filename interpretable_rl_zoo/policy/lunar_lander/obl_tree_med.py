def play(x):
    if (x[3] - x[4]) <= -0.09369609132409096:
        if (x[2] - x[5]) <= -0.15045850723981857:
            if x[4] <= -0.09304802492260933:
                return 2
            else:
                return 3
        else:
            if x[3] <= -0.20931557565927505:
                if (x[4] - x[7]) <= 0.05314052663743496:
                    return 2
                else:
                    if (x[2] - x[5]) <= 0.12694627046585083:
                        return 3
                    else:
                        return 2
            else:
                if (x[0] - x[4]) <= -0.005620334763079882:
                    if (x[2] - x[4]) <= 0.07193982228636742:
                        return 3
                    else:
                        return 2
                else:
                    if (x[1] - x[4]) <= 0.6290301382541656:
                        return 2
                    else:
                        return 1
    else:
        if (x[0] - x[7]) <= -0.8069067299365997:
            return 0
        else:
            if x[3] <= -0.2254307121038437:
                if (x[4] - x[5]) <= -0.3484945595264435:
                    return 1
                else:
                    return 2
            else:
                if x[4] <= -0.03889779560267925:
                    return 1
                else:
                    if (x[3] - x[4]) <= 1.7299442291259766:
                        if (x[2] - x[5]) <= -0.0015266332775354385:
                            return 3
                        else:
                            return 1
                    else:
                        return 1


metadata =  {"algorithm": "PPO", "env_name": "LunarLander-v2"}
