def play(x):
    h_layer_0_0 = (
        -1.597325889849925 * x[0]
        + 0.05755507567778703 * x[1]
        + -2.4891078457073816 * x[2]
        + -0.411525583842316 * x[3]
        + 5.516955937587083 * x[4]
        + 2.7388193889147856 * x[5]
        + -0.060694422831123536 * x[6]
        + -0.6494391326681663 * x[7]
        + 0.192680602750433
    )
    h_layer_0_0 = max(0.0, h_layer_0_0)
    h_layer_0_1 = (
        1.9459138044316215 * x[0]
        + 0.8529392900082133 * x[1]
        + 1.7326278305740246 * x[2]
        + 4.348855060333114 * x[3]
        + -5.299298419417898 * x[4]
        + -1.8257877538283833 * x[5]
        + 1.764932373043007 * x[6]
        + 0.771103749936964 * x[7]
        + 0.8177583905541449
    )
    h_layer_0_1 = max(0.0, h_layer_0_1)
    h_layer_0_2 = (
        -1.0746115472804838 * x[0]
        + 0.07767402822155381 * x[1]
        + -1.7334011979522757 * x[2]
        + 2.394547473184642 * x[3]
        + 3.7721225973680292 * x[4]
        + 3.5755040840516177 * x[5]
        + 0.30594367911086884 * x[6]
        + 0.5151027377862257 * x[7]
        + 0.46348442529799144
    )
    h_layer_0_2 = max(0.0, h_layer_0_2)
    h_layer_0_3 = (
        -1.6330798493882892 * x[0]
        + -0.15340971611183976 * x[1]
        + -1.917435663881706 * x[2]
        + 0.0692751678300117 * x[3]
        + 5.703580482459034 * x[4]
        + 5.519554718306904 * x[5]
        + 0.46198417670979164 * x[6]
        + 0.5467552633597438 * x[7]
        + 1.0653607345953588
    )
    h_layer_0_3 = max(0.0, h_layer_0_3)
    h_layer_0_4 = (
        -0.022563506859959764 * x[0]
        + -0.409583900817303 * x[1]
        + 0.6315928429866154 * x[2]
        + -0.2957568198242025 * x[3]
        + -0.6176752271357075 * x[4]
        + -1.3861243249945039 * x[5]
        + 0.7563574359576103 * x[6]
        + 2.264440479514898 * x[7]
        + 0.3603665474086783
    )
    h_layer_0_4 = max(0.0, h_layer_0_4)
    h_layer_0_5 = (
        -0.8652439066593502 * x[0]
        + 0.057398010343299534 * x[1]
        + -1.2949664248325583 * x[2]
        + -0.7325505550978946 * x[3]
        + 2.834204835196404 * x[4]
        + 1.3145442858870462 * x[5]
        + -0.1639456640135979 * x[6]
        + 0.1348604253834723 * x[7]
        + -0.23889623243598507
    )
    h_layer_0_5 = max(0.0, h_layer_0_5)
    h_layer_0_6 = (
        -0.47628617805705026 * x[0]
        + -0.40420930399040167 * x[1]
        + 0.027369767251341284 * x[2]
        + -4.519121382602946 * x[3]
        + 1.429062212448073 * x[4]
        + 0.5401735895246308 * x[5]
        + 0.16241347257505212 * x[6]
        + 0.17682949772961845 * x[7]
        + -0.17651253727833835
    )
    h_layer_0_6 = max(0.0, h_layer_0_6)
    h_layer_0_7 = (
        0.4617751634680622 * x[0]
        + -0.0016168015949702217 * x[1]
        + 0.8513800069123948 * x[2]
        + -3.5436141628232076 * x[3]
        + -1.6984739395253545 * x[4]
        + -3.319230025529502 * x[5]
        + -0.04784920124392181 * x[6]
        + -0.027752785814578483 * x[7]
        + 0.0017776820611063997
    )
    h_layer_0_7 = max(0.0, h_layer_0_7)

    h_layer_1_0 = (
        0.35833788113400267 * h_layer_0_0
        + -3.5803414904514246 * h_layer_0_1
        + -5.157824851601022 * h_layer_0_2
        + -0.49223151438030416 * h_layer_0_3
        + -0.44771753452249735 * h_layer_0_4
        + -0.6216564017634328 * h_layer_0_5
        + 4.446123259620291 * h_layer_0_6
        + 2.421813233302289 * h_layer_0_7
        + -0.26660007565691757
    )
    h_layer_1_0 = max(0.0, h_layer_1_0)
    h_layer_1_1 = (
        -1.5620904206888022 * h_layer_0_0
        + -2.2627348115565353 * h_layer_0_1
        + 3.858066627002753 * h_layer_0_2
        + 4.078649538165368 * h_layer_0_3
        + 1.031320942360873 * h_layer_0_4
        + -2.0568957880222034 * h_layer_0_5
        + 0.8672816361002527 * h_layer_0_6
        + -1.0964264277405613 * h_layer_0_7
        + 0.26937470317805307
    )
    h_layer_1_1 = max(0.0, h_layer_1_1)
    h_layer_1_2 = (
        3.0095372736868593 * h_layer_0_0
        + -4.778501882095135 * h_layer_0_1
        + 8.108011947413129 * h_layer_0_2
        + 3.8884676785182894 * h_layer_0_3
        + -0.9362036302621086 * h_layer_0_4
        + 1.7368225140903293 * h_layer_0_5
        + 0.20971012005216252 * h_layer_0_6
        + -0.7998898928542861 * h_layer_0_7
        + -0.09555836686434542
    )
    h_layer_1_2 = max(0.0, h_layer_1_2)
    h_layer_1_3 = (
        -8.74612086e-316 * h_layer_0_0
        + 6.1659549e-316 * h_layer_0_1
        + 3.4490403e-316 * h_layer_0_2
        + -1.8286875e-316 * h_layer_0_3
        + -7.26346523e-316 * h_layer_0_4
        + 4.65399322e-315 * h_layer_0_5
        + -2.94183286e-315 * h_layer_0_6
        + -3.521020914e-315 * h_layer_0_7
        + -0.3461953938684081
    )
    h_layer_1_3 = max(0.0, h_layer_1_3)
    h_layer_1_4 = (
        3.36389796e-315 * h_layer_0_0
        + 7.366019e-317 * h_layer_0_1
        + 6.5173873e-316 * h_layer_0_2
        + 1.41884027e-315 * h_layer_0_3
        + -3.04320095e-316 * h_layer_0_4
        + -3.29085741e-315 * h_layer_0_5
        + -1.880372327e-315 * h_layer_0_6
        + 2.256139655e-315 * h_layer_0_7
        + -0.3959442640108323
    )
    h_layer_1_4 = max(0.0, h_layer_1_4)
    h_layer_1_5 = (
        -1.1665523740098278 * h_layer_0_0
        + -2.3201156621933436 * h_layer_0_1
        + -11.34411603608459 * h_layer_0_2
        + 0.3573814570975038 * h_layer_0_3
        + 0.70782594081949 * h_layer_0_4
        + -1.133529192847794 * h_layer_0_5
        + 3.259304181674498 * h_layer_0_6
        + 3.078735918805726 * h_layer_0_7
        + -0.8480215258649321
    )
    h_layer_1_5 = max(0.0, h_layer_1_5)
    h_layer_1_6 = (
        -3.025220673e-315 * h_layer_0_0
        + -1.117458543e-315 * h_layer_0_1
        + -2.59934764e-315 * h_layer_0_2
        + -2.61283298e-315 * h_layer_0_3
        + 3.92909872e-315 * h_layer_0_4
        + 3.92194463e-316 * h_layer_0_5
        + -3.519165614e-315 * h_layer_0_6
        + 5.35373234e-316 * h_layer_0_7
        + -0.21653653468532258
    )
    h_layer_1_6 = max(0.0, h_layer_1_6)
    h_layer_1_7 = (
        5.0519516e-316 * h_layer_0_0
        + 8.0335735e-316 * h_layer_0_1
        + 3.179923496e-315 * h_layer_0_2
        + 3.720472073e-315 * h_layer_0_3
        + -1.220265204e-315 * h_layer_0_4
        + 4.83176726e-315 * h_layer_0_5
        + -2.189067477e-315 * h_layer_0_6
        + -1.29244359e-315 * h_layer_0_7
        + -0.5853275126100634
    )
    h_layer_1_7 = max(0.0, h_layer_1_7)

    h_layer_2_0 = (
        -13.428754724074816 * h_layer_1_0
        + 6.29478895513926 * h_layer_1_1
        + -4.699181479454222 * h_layer_1_2
        + -4.53771959e-315 * h_layer_1_3
        + 6.53835196e-316 * h_layer_1_4
        + -3.864980855880964 * h_layer_1_5
        + -3.47181078e-315 * h_layer_1_6
        + 4.872879723e-315 * h_layer_1_7
        + -0.6919000998794629
    )
    y_0 = h_layer_2_0
    h_layer_2_1 = (
        -21.290700237284657 * h_layer_1_0
        + -1.0853760790619866 * h_layer_1_1
        + -25.295328835575315 * h_layer_1_2
        + 4.108723205e-315 * h_layer_1_3
        + 5.14534687e-316 * h_layer_1_4
        + -2.3402005993107653 * h_layer_1_5
        + 8.601885e-317 * h_layer_1_6
        + -4.3727455e-315 * h_layer_1_7
        + 19.852134243428445
    )
    y_1 = h_layer_2_1
    h_layer_2_2 = (
        12.661376038500165 * h_layer_1_0
        + -0.9654023242556695 * h_layer_1_1
        + -5.44078129265403 * h_layer_1_2
        + -1.052095594e-315 * h_layer_1_3
        + 2.24510534e-316 * h_layer_1_4
        + 12.543552147261703 * h_layer_1_5
        + 2.920806e-315 * h_layer_1_6
        + -2.224613183e-315 * h_layer_1_7
        + -3.214159932942397
    )
    y_2 = h_layer_2_2
    h_layer_2_3 = (
        -1.6013937464152583 * h_layer_1_0
        + -4.396283946155449 * h_layer_1_1
        + 13.397696794952513 * h_layer_1_2
        + -1.57294e-316 * h_layer_1_3
        + -5.64093834e-316 * h_layer_1_4
        + -12.560485560061675 * h_layer_1_5
        + 2.195827e-315 * h_layer_1_6
        + -9.26676536e-316 * h_layer_1_7
        + -12.860546439767296
    )
    y_3 = h_layer_2_3

    max_val = y_0
    action = 0
    if y_1 > max_val:
        max_val = y_1
        action = 1
    if y_2 > max_val:
        max_val = y_2
        action = 2
    if y_3 > max_val:
        action = 3
    return action


metadata =  {"algorithm": "PPO", "env_name": "LunarLander-v2"}
