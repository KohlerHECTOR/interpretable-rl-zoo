from math import exp


def play(x):
    h_layer_0_0 = (
        0.6468305634732882 * x[0] + -2.4385899726527054 * x[1] + -0.21581192958573162
    )
    h_layer_0_0 = max(0.0, h_layer_0_0)
    h_layer_0_1 = (
        0.7039096498079792 * x[0] + -2.5302576830851593 * x[1] + -0.23958982505019866
    )
    h_layer_0_1 = max(0.0, h_layer_0_1)

    h_layer_1_0 = (
        -1.305051307082277e-13 * h_layer_0_0
        + 4.0837910986095266e-08 * h_layer_0_1
        + -1.0739992424604454
    )
    h_layer_1_0 = max(0.0, h_layer_1_0)
    h_layer_1_1 = (
        3.508868044593161 * h_layer_0_0
        + 2.9947224474101835 * h_layer_0_1
        + -0.12937394324963242
    )
    h_layer_1_1 = max(0.0, h_layer_1_1)

    h_layer_2_0 = (
        -3.3017609242891726e-175 * h_layer_1_0
        + -3.045490137195551 * h_layer_1_1
        + 6.782913701828734
    )
    y_0 = h_layer_2_0

    if 1 / (1 + exp(-y_0)) >= 0.5:
        return 2
    else:
        return 0


metadata =  {"algorithm": "PPO", "env_name": "MountainCar-v0"}
