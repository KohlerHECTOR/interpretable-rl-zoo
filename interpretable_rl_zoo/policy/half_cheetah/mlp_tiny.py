def play(x):
    h_layer_0_0 = (
        3.406032039408604 * x[0]
        + -0.2892330451467799 * x[1]
        + 0.4206300543592947 * x[2]
        + 0.3640866470225191 * x[3]
        + 1.0201599049967507 * x[4]
        + 0.33685456461670943 * x[5]
        + 0.6647229453822681 * x[6]
        + 0.5524399527609015 * x[7]
        + -0.012216800153765556 * x[8]
        + 0.2985979850701528 * x[9]
        + -0.21532205777219082 * x[10]
        + -0.061903916121251075 * x[11]
        + 0.007531841475067727 * x[12]
        + -0.007136136153480225 * x[13]
        + 0.005765054819072181 * x[14]
        + -8.18126326774555e-05 * x[15]
        + -0.004769077166053735 * x[16]
        + 1.3496615204133324
    )
    h_layer_0_0 = max(0.0, h_layer_0_0)
    h_layer_0_1 = (
        -1.1710113745512507 * x[0]
        + 0.5239054146651067 * x[1]
        + 1.1271425810721194 * x[2]
        + -1.5990670258623543 * x[3]
        + -0.16277837304603054 * x[4]
        + 1.1830789009698544 * x[5]
        + -1.03837527493415 * x[6]
        + -1.033863408562216 * x[7]
        + -0.10312647355810833 * x[8]
        + -0.08513368140258296 * x[9]
        + 0.5797131280115756 * x[10]
        + 0.043129388099709655 * x[11]
        + 0.06832323379503709 * x[12]
        + -0.050418849563760075 * x[13]
        + 0.07480674557842792 * x[14]
        + 0.03206654583958322 * x[15]
        + 0.02990155655852622 * x[16]
        + -0.17780478230804347
    )
    h_layer_0_1 = max(0.0, h_layer_0_1)

    h_layer_1_0 = (
        -0.2784434885357482 * h_layer_0_0
        + -0.9218446223349781 * h_layer_0_1
        + 1.2569707817152342
    )
    h_layer_1_0 = max(0.0, h_layer_1_0)
    h_layer_1_1 = (
        -1.270924834693758 * h_layer_0_0
        + 0.14966350856146862 * h_layer_0_1
        + 0.9601396547164031
    )
    h_layer_1_1 = max(0.0, h_layer_1_1)

    h_layer_2_0 = (
        1.001353458150705 * h_layer_1_0
        + -0.227315681108722 * h_layer_1_1
        + -0.6399084296695154
    )
    y_0 = h_layer_2_0
    h_layer_2_1 = (
        -0.5773760119826086 * h_layer_1_0
        + -0.8873337440811098 * h_layer_1_1
        + 0.9575330763235035
    )
    y_1 = h_layer_2_1
    h_layer_2_2 = (
        0.792088673106238 * h_layer_1_0
        + 0.6749614870104753 * h_layer_1_1
        + -0.7442415837864542
    )
    y_2 = h_layer_2_2
    h_layer_2_3 = (
        -0.6338225344271845 * h_layer_1_0
        + 0.7454572822537554 * h_layer_1_1
        + 0.21244417422370462
    )
    y_3 = h_layer_2_3
    h_layer_2_4 = (
        -1.260066423503151 * h_layer_1_0
        + -0.16507859962926383 * h_layer_1_1
        + 0.6619921713450537
    )
    y_4 = h_layer_2_4
    h_layer_2_5 = (
        -0.5504949954146667 * h_layer_1_0
        + -0.4768553200854484 * h_layer_1_1
        + 0.32579257754359314
    )
    y_5 = h_layer_2_5

    return [y_0, y_1, y_2, y_3, y_4, y_5]


metadata =  {"algorithm": "SAC", "env_name": "HalfCheetah-v3"}
