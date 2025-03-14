def play(x):
    h_layer_0_0 = (
        -1.5122647228885409 * x[0]
        + -0.5995411150363686 * x[1]
        + -0.1705476647902998 * x[2]
        + 0.05362928081518453 * x[3]
        + -1.0088749589613217 * x[4]
        + 0.14556637424080265 * x[5]
        + 0.37472552065199366 * x[6]
        + 0.10128720722866207 * x[7]
        + 1.400700991614072
    )
    h_layer_0_0 = max(0.0, h_layer_0_0)
    h_layer_0_1 = (
        -2.2693463718397693 * x[0]
        + 0.30003264732099794 * x[1]
        + -0.5268577060848806 * x[2]
        + 0.033183581958088466 * x[3]
        + -0.6370606806470824 * x[4]
        + -0.054615941858350094 * x[5]
        + 0.7126517773102995 * x[6]
        + -0.2017027852334677 * x[7]
        + 0.20567134886665633
    )
    h_layer_0_1 = max(0.0, h_layer_0_1)

    h_layer_1_0 = (
        1.5048921584064126 * h_layer_0_0
        + -0.9305601345229961 * h_layer_0_1
        + -0.7480278397734536
    )
    h_layer_1_0 = max(0.0, h_layer_1_0)
    h_layer_1_1 = (
        1.4000300239411345 * h_layer_0_0
        + -1.3166884448025682 * h_layer_0_1
        + -0.019426591857589114
    )
    h_layer_1_1 = max(0.0, h_layer_1_1)

    h_layer_2_0 = (
        -1.97404150013711 * h_layer_1_0
        + 1.5310421826952934 * h_layer_1_1
        + 0.156110928025513
    )
    y_0 = h_layer_2_0
    h_layer_2_1 = (
        1.7802093688387208 * h_layer_1_0
        + -1.9410649715596238 * h_layer_1_1
        + 0.5328101300941412
    )
    y_1 = h_layer_2_1

    return [y_0, y_1]


metadata =  {"algorithm": "SAC", "env_name": "Swimmer-v3"}
