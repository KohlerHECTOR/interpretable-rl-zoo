def play(x):
    h_layer_0_0 = (
        -0.14220680144900344 * x[0]
        + -0.10247131056767089 * x[1]
        + -0.03164079725417257 * x[2]
        + 0.07514509146477007 * x[3]
        + -0.07261791470088326 * x[4]
        + -0.19639742607994126 * x[5]
        + -0.2641597925105892 * x[6]
        + -0.0034501250845755454 * x[7]
        + 0.031599810702495894 * x[8]
        + 0.006104363598794427 * x[9]
        + 0.05712457711394849 * x[10]
        + 0.08924030622235521 * x[11]
        + 0.012000248487750957 * x[12]
        + 0.006288662143153223 * x[13]
        + -0.11325345479459833 * x[14]
        + 0.1053054754656038 * x[15]
        + -0.07076697856857035 * x[16]
        + 0.03754250690612434 * x[17]
        + -0.10817758589435358 * x[18]
        + -0.158581879056025 * x[19]
        + 0.0950660077674923 * x[20]
        + 0.12770637057043852 * x[21]
        + -0.188038097005609 * x[22]
        + -0.2647849209489441 * x[23]
        + 0.9393061543835787
    )
    h_layer_0_0 = max(0.0, h_layer_0_0)
    h_layer_0_1 = (
        -0.5060319243086411 * x[0]
        + 0.18058825698432363 * x[1]
        + 0.24424204821968154 * x[2]
        + 0.03452972159077805 * x[3]
        + -0.3219592524080186 * x[4]
        + 0.0940307359696328 * x[5]
        + -0.08905674046702194 * x[6]
        + -0.04866359290418789 * x[7]
        + -0.10056164329026486 * x[8]
        + -0.09729937065020434 * x[9]
        + -0.03349413422517952 * x[10]
        + 0.4402541146055462 * x[11]
        + -0.15574542998728877 * x[12]
        + 0.25707343738562216 * x[13]
        + 0.31795712162156875 * x[14]
        + -0.16221832158990337 * x[15]
        + 0.022707895711855643 * x[16]
        + -0.06352855542938043 * x[17]
        + -0.11274387866717414 * x[18]
        + -0.07106631347338403 * x[19]
        + -0.17910463201567664 * x[20]
        + -0.10286292504000263 * x[21]
        + 0.08730520939248788 * x[22]
        + 0.18912243255351915 * x[23]
        + 1.3717325199744088
    )
    h_layer_0_1 = max(0.0, h_layer_0_1)

    h_layer_1_0 = (
        -1.098582109118276 * h_layer_0_0
        + -0.05258689952708522 * h_layer_0_1
        + 1.3916465170243941
    )
    h_layer_1_0 = max(0.0, h_layer_1_0)
    h_layer_1_1 = (
        0.34567933633735876 * h_layer_0_0
        + 0.9954544777635278 * h_layer_0_1
        + -0.05946741320531873
    )
    h_layer_1_1 = max(0.0, h_layer_1_1)

    h_layer_2_0 = (
        0.07650858474706461 * h_layer_1_0
        + 0.5396328138245751 * h_layer_1_1
        + -0.5943812796540217
    )
    y_0 = h_layer_2_0
    h_layer_2_1 = (
        -1.4014078714352827 * h_layer_1_0
        + -0.25821054724769543 * h_layer_1_1
        + 1.4382703355771882
    )
    y_1 = h_layer_2_1
    h_layer_2_2 = (
        -0.40391720419039717 * h_layer_1_0
        + -0.3844780760008261 * h_layer_1_1
        + 0.8484071156097018
    )
    y_2 = h_layer_2_2
    h_layer_2_3 = (
        -0.8056068039683809 * h_layer_1_0
        + -0.6315358382759892 * h_layer_1_1
        + 1.1702202127938757
    )
    y_3 = h_layer_2_3

    return [y_0, y_1, y_2, y_3]


metadata =  {"algorithm": "PPO", "env_name": "BipedalWalker-v3"}
