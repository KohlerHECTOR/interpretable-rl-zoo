def play(x):
    if x[4] <= -0.3189932107925415:
        if x[0] <= 0.33446820080280304:
            if x[1] <= 0.9190371334552765:
                if x[1] <= 0.02829295489937067:
                    return [-0.7839363104749878, -0.9105621518363722]
                else:
                    return [-0.8844636044431844, -0.6746865962957365]
            else:
                return [-0.6918405068744637, -0.005338977602496617]
        else:
            if x[1] <= -0.7971687018871307:
                return [-0.07824547474594723, -0.8799999691857937]
            else:
                return [0.6220877478176272, -0.8137545780695491]
    else:
        if x[4] <= 0.7156983017921448:
            if x[0] <= -0.5562731325626373:
                if x[0] <= -1.897627592086792:
                    return [0.7617911462528444, -0.7863940917994287]
                else:
                    if x[2] <= 0.049365684390068054:
                        if x[0] <= -1.2304846048355103:
                            return [-0.24285228410679008, 0.8837962458034961]
                        else:
                            if x[1] <= 1.7315903902053833:
                                return [0.052607108938493734, 0.9433308611866861]
                            else:
                                return [0.779601244216617, 0.9337038114213905]
                    else:
                        return [-0.4005293359503078, 0.6250995058112419]
            else:
                if x[2] <= -0.3522292226552963:
                    return [0.628743950660675, 0.06966834596474045]
                else:
                    return [0.2812487645076557, -0.7026785693571865]
        else:
            if x[3] <= 0.6164935529232025:
                if x[2] <= -0.7489741146564484:
                    return [0.8884682181441197, 0.8604946273706204]
                else:
                    return [0.7628416408062824, 0.10043228030520605]
            else:
                if x[2] <= -1.2474998831748962:
                    return [-0.38915680517212614, 0.9578880862212081]
                else:
                    return [0.7499457989608178, 0.9317937326446312]


metadata =  {"algorithm": "SAC", "env_name": "Swimmer-v3"}
