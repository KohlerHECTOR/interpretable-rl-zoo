def play(x):
    h_layer_0_0 = (
        1.3414795764639462 * x[0]
        + 1.0322924665892161 * x[1]
        + -0.09078184878143603 * x[2]
        + 0.07783691333628368 * x[3]
        + 0.5224258388149264 * x[4]
        + 0.43278429513234773 * x[5]
        + 0.05308695072477953 * x[6]
        + 0.05274789008485497 * x[7]
        + 0.46954620854492124
    )
    h_layer_0_0 = max(0.0, h_layer_0_0)
    h_layer_0_1 = (
        1.7217441884635016 * x[0]
        + -0.04934572595118616 * x[1]
        + 0.6425191482736036 * x[2]
        + 0.752242659416577 * x[3]
        + 0.12230940014364267 * x[4]
        + 0.15078967702897236 * x[5]
        + 0.021403194504074206 * x[6]
        + 0.2418469827994376 * x[7]
        + -0.06588529740440212
    )
    h_layer_0_1 = max(0.0, h_layer_0_1)
    h_layer_0_2 = (
        -0.018826968895382833 * x[0]
        + 1.3301600444600103 * x[1]
        + -0.5263569686996468 * x[2]
        + -0.8549055956298484 * x[3]
        + 1.1607418258409343 * x[4]
        + 0.19226813173665563 * x[5]
        + -0.02822656913526697 * x[6]
        + 0.21708782000513369 * x[7]
        + 1.3896226757764913
    )
    h_layer_0_2 = max(0.0, h_layer_0_2)
    h_layer_0_3 = (
        -0.6053071353151597 * x[0]
        + 0.4511067167243234 * x[1]
        + -1.607427105880951 * x[2]
        + 0.06500814580333329 * x[3]
        + 0.9361135078107056 * x[4]
        + -0.2138210287827373 * x[5]
        + -0.495723332496774 * x[6]
        + -0.27300230985074203 * x[7]
        + 0.9786831324457022
    )
    h_layer_0_3 = max(0.0, h_layer_0_3)

    h_layer_1_0 = (
        -1.1117224001094719 * h_layer_0_0
        + -3.913496346900476e-06 * h_layer_0_1
        + 0.6834473127536599 * h_layer_0_2
        + -1.6972615846233587 * h_layer_0_3
        + -0.09426446864393487
    )
    h_layer_1_0 = max(0.0, h_layer_1_0)
    h_layer_1_1 = (
        -0.6775579645996267 * h_layer_0_0
        + -0.0950958457555564 * h_layer_0_1
        + 0.7226182095974768 * h_layer_0_2
        + -0.6192220979921614 * h_layer_0_3
        + 0.03622431269321747
    )
    h_layer_1_1 = max(0.0, h_layer_1_1)
    h_layer_1_2 = (
        -2.538720347982667 * h_layer_0_0
        + -0.5261749537234096 * h_layer_0_1
        + -0.13060572666982231 * h_layer_0_2
        + 0.2749896963812599 * h_layer_0_3
        + 0.9190893015405736
    )
    h_layer_1_2 = max(0.0, h_layer_1_2)
    h_layer_1_3 = (
        -0.701992464335276 * h_layer_0_0
        + 0.026984175197049022 * h_layer_0_1
        + -0.1607743959519907 * h_layer_0_2
        + 1.019497372539035 * h_layer_0_3
        + -0.6452231739677564
    )
    h_layer_1_3 = max(0.0, h_layer_1_3)

    h_layer_2_0 = (
        -0.3778742648678638 * h_layer_1_0
        + 0.0031469574603863143 * h_layer_1_1
        + -1.9476976206550463 * h_layer_1_2
        + 0.05259915887820291 * h_layer_1_3
        + 0.8328641216864796
    )
    y_0 = h_layer_2_0
    h_layer_2_1 = (
        -1.6353957619568102 * h_layer_1_0
        + 1.4790332924973981 * h_layer_1_1
        + -0.045551470829190706 * h_layer_1_2
        + 1.3237598308925582 * h_layer_1_3
        + -0.9148868644547488
    )
    y_1 = h_layer_2_1

    return [y_0, y_1]


metadata =  {"algorithm": "SAC", "env_name": "Swimmer-v3"}
