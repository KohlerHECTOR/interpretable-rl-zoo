def play(x):
    if (x[0] - x[4]) <= -0.004492944106459618:
        if (x[2] - x[4]) <= -0.0446188822388649:
            if x[3] <= -0.2753435969352722:
                return 2
            else:
                if (x[0] - x[4]) <= -0.04057411476969719:
                    return 3
                else:
                    return 3
        else:
            if (x[5] - x[6]) <= -0.8438796699047089:
                if x[4] <= -0.3175402283668518:
                    return 1
                else:
                    return 0
            else:
                if x[5] <= 0.020287134684622288:
                    if (x[3] - x[6]) <= -0.16681358218193054:
                        if (x[1] - x[4]) <= 1.3924201130867004:
                            if (x[3] - x[7]) <= -0.22904131561517715:
                                return 2
                            else:
                                if (x[1] - x[4]) <= 0.8353906273841858:
                                    return 2
                                else:
                                    return 1
                        else:
                            return 1
                    else:
                        if (x[2] - x[4]) <= 0.07794278487563133:
                            return 3
                        else:
                            return 1
                else:
                    if (x[2] - x[4]) <= 0.10085860639810562:
                        return 3
                    else:
                        if (x[5] - x[7]) <= 0.1520889699459076:
                            if x[3] <= -0.218589685857296:
                                return 2
                            else:
                                return 1
                        else:
                            return 3
    else:
        if (x[0] - x[7]) <= -0.815377801656723:
            if (x[2] - x[4]) <= 0.088236503303051:
                return 0
            else:
                return 1
        else:
            if (x[3] - x[4]) <= -0.12272932007908821:
                if (x[2] - x[5]) <= -0.058593375608325005:
                    if x[4] <= -0.019619527272880077:
                        return 2
                    else:
                        if (x[1] - x[7]) <= 1.4987189173698425:
                            return 3
                        else:
                            return 1
                else:
                    if (x[0] - x[4]) <= 0.1580980196595192:
                        if (x[1] - x[4]) <= 1.2578462958335876:
                            if x[3] <= -0.15172691643238068:
                                if (x[4] - x[7]) <= 0.03614983335137367:
                                    return 2
                                else:
                                    return 2
                            else:
                                return 0
                        else:
                            if (x[3] - x[7]) <= -0.28377991914749146:
                                return 2
                            else:
                                return 1
                    else:
                        if (x[3] - x[7]) <= -0.21051577478647232:
                            if (x[1] - x[7]) <= 1.2220520377159119:
                                return 2
                            else:
                                return 1
                        else:
                            return 1
            else:
                if x[3] <= -0.32117682695388794:
                    return 2
                else:
                    if (x[1] - x[4]) <= 0.055533187463879585:
                        return 0
                    else:
                        if (x[3] - x[4]) <= -0.017336290329694748:
                            return 1
                        else:
                            return 1


metadata =  {"algorithm": "PPO", "env_name": "LunarLander-v2"}
