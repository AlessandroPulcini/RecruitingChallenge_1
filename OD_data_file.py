# Object detection project, data file

# ******************* INPUT DATA *******************
# Original photo dimensions
photo_dim_1 = [1200, 800]
photo_dim_2 = [1200, 800]
photo_dim_3 = [900, 1200]
photo_dim_error_test = [200, 800]

# Raw data
data_1 = \
    [
        [
            [
                [0.95, 10, 10, 100, 100, 0.1, 0.1, 0.8],  # Box 1
                [0.90, 10, 20, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ],  # 1st square in the row
            [
                [0.85, 10, 10, 100, 100, 0.1, 0.8, 0.1],  # Box 1
                [0.85, 10, 20, 100, 100, 0.1, 0.8, 0.1]  # Box 2
            ],  # 2nd square in the row
            [
                [0.10, 10, 10, 100, 100, 0.1, 0.1, 0.8],  # Box 1
                [0.20, 10, 20, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ],  # 3rd square in the row
        ],  # 1st row
        [
            [
                [0.95, 10, 10, 100, 100, 0.1, 0.1, 0.8],  # Box 1
                [0.90, 10, 20, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ],  # 1st square in the row
            [
                [0.75, 10, 10, 100, 100, 0.8, 0.1, 0.1],  # Box 1
                [0.80, 10, 20, 100, 100, 0.8, 0.1, 0.1]  # Box 2
            ],  # 2nd square in the row
            [
                [0.10, 10, 10, 100, 100, 0.2, 0.4, 0.4],  # Box 1
                [0.00, 10, 20, 100, 100, 0.2, 0.4, 0.4]  # Box 2
            ]  # 3rd square in the row
        ]  # 2nd row
    ]

data_2 = \
    [
        [
            [
                [0.95, 120, 75, 100, 100, 0.1, 0.1, 0.7, 0.1],  # Box 1
                [0.90, 110, 70, 100, 100, 0.1, 0.1, 0.7, 0.1]  # Box 2
            ],  # 1st square in the row
            [
                [0.85, 60, 260, 100, 100, 0.8, 0.15, 0.05, 0.],  # Box 1
                [0.85, 70, 250, 100, 100, 0.85, 0.15, 0.0, 0.]  # Box 2
            ],  # 2nd square in the row
            [
                [0.20, 200, 300, 100, 100, 0.1, 0.05, 0.05, 0.8],  # Box 1
                [0.20, 210, 300, 100, 100, 0.1, 0.05, 0.05, 0.8]  # Box 2
            ],  # 3rd square in the row
        ],  # 1st row
        [
            [
                [0.95, 180, 320, 100, 100, 0., 0.05, 0.15, 0.8],  # Box 1
                [0.90, 190, 320, 100, 100, 0., 0., 0.1, 0.9]  # Box 2
            ],  # 1st square in the row
            [
                [0.75, 390, 130, 100, 100, 0.65, 0.3, 0.05, 0],  # Box 1
                [0.80, 390, 120, 100, 100, 0.65, 0.3, 0.05, 0]  # Box 2
            ],  # 2nd square in the row
            [
                [0.85, 10, 125, 100, 100, 0.2, 0.7, 0.1, 0],  # Box 1
                [0.80, 10, 120, 100, 100, 0.2, 0.7, 0.1, 0]  # Box 2
            ]  # 3rd square in the row
        ]  # 2nd row
    ]

data_3 = \
    [
        [
            [
                [0.90, 298, 70, 100, 20, 0.1, 0.1, 0.8],  # Box 1
                [0.85, 299, 70, 90, 23, 0.1, 0.1, 0.8],  # Box 2
                [0.85, 299, 70, 90, 20, 0.1, 0.1, 0.8]  # Box 3
            ],  # 1st square in the row
            [
                [0.85, 1, 70, 96, 20, 0.1, 0.1, 0.8],  # Box 1
                [0.85, 2, 70, 100, 50, 0.1, 0.1, 0.8],  # Box 2
                [0.80, 2, 70, 96, 50, 0.1, 0.1, 0.8]  # Box 3
            ],  # 2nd square in the row
            [
                [0.70, 170, 298, 50, 50, 0.1, 0.1, 0.8],  # Box 1
                [0.65, 175, 296, 50, 50, 0.1, 0.1, 0.8],  # Box 2
                [0.65, 175, 298, 50, 60, 0.1, 0.1, 0.8]  # Box 3
            ],  # 3rd square in the row
        ],  # 1st row
        [
            [
                [0.15, 210, 170, 70, 70, 0.1, 0.1, 0.8],  # Box 1
                [0.10, 216, 170, 70, 70, 0.1, 0.1, 0.8],  # Box 2
                [0.15, 220, 170, 70, 70, 0.1, 0.1, 0.8]  # Box 3
            ],  # 1st square in the row
            [
                [0.75, 160, 90, 60, 50, 0.0, 0.1, 0.9],  # Box 1
                [0.80, 166, 80, 60, 50, 0.0, 0.1, 0.9],  # Box 2
                [0.75, 166, 86, 60, 50, 0.0, 0.1, 0.9]  # Box 3
            ],  # 2nd square in the row
            [
                [0.70, 176, 2, 50, 50, 0.1, 0.1, 0.8],  # Box 1
                [0.65, 170, 0, 50, 50, 0.05, 0.1, 0.85],  # Box 2
                [0.65, 170, 2, 50, 50, 0.05, 0.1, 0.85]  # Box 3
            ]  # 3rd square in the row
        ],  # 2dn row
        [
            [
                [0.05, 100, 100, 50, 80, 0.1, 0.1, 0.8],  # Box 1
                [0.10, 106, 106, 50, 80, 0.1, 0.1, 0.8],  # Box 2
                [0.15, 100, 110, 55, 80, 0.1, 0.1, 0.8]  # Box 3
            ],  # 1st square in the row
            [
                [0.75, 10, 10, 100, 100, 0.8, 0.1, 0.1],  # Box 1
                [0.80, 10, 20, 100, 100, 0.8, 0.1, 0.1],  # Box 2
                [0.80, 10, 26, 100, 100, 0.75, 0.15, 0.1]  # Box 2
            ],  # 2nd square in the row
            [
                [0.90, 100, 250, 80, 80, 0.0, 0.5, 0.5],  # Box 1
                [0.85, 100, 260, 80, 80, 0.0, 0.5, 0.5],  # Box 2
                [0.85, 104, 260, 80, 80, 0.0, 0.6, 0.4]  # Box 2
            ]  # 3rd square in the row
        ],  # 3rd row
        [
            [
                [0.95, 290, 10, 90, 90, 0.8, 0.2, 0.0],  # Box 1
                [0.90, 284, 20, 90, 90, 0.8, 0.2, 0.0],  # Box 2
                [0.90, 284, 20, 90, 90, 0.8, 0.2, 0.0]  # Box 2
            ],  # 1st square in the row
            [
                [0.10, 10, 10, 70, 70, 0.3, 0.4, 0.3],  # Box 1
                [0.10, 10, 20, 70, 70, 0.3, 0.4, 0.3],  # Box 2
                [0.05, 6, 20, 70, 70, 0.3, 0.4, 0.3]  # Box 2
            ],  # 2nd square in the row
            [
                [0.6, 10, 220, 70, 70, 0.2, 0.0, 0.8],  # Box 1
                [0.6, 10, 220, 70, 70, 0.2, 0.0, 0.8],  # Box 2
                [0.6, 10, 220, 70, 70, 0.2, 0.0, 0.8]  # Box 2
            ]  # 3rd square in the row
        ]  # 4th row
    ]

ragged_data_1 = \
    [
        [
            [
                [0.95, 10, 10, 100, 100, 0.1],  # Box 1
                [0.90, 10, 20, 100, 100, 0.1]  # Box 2
            ]  # 1st square in the row, missing 2nd square in the row
        ],  # 1st row
        [
            [
                [0.95, 10, 10, 100, 100, 0.1],  # Box 1
                [0.90, 10, 20, 100, 100, 0.1]  # Box 2
            ],  # 1st square in the row
            [
                [0.75, 10, 10, 100, 100, 0.8],  # Box 1
                [0.80, 10, 20, 100, 100, 0.8]  # Box 2
            ]  # 2nd square in the row
        ]  # 2nd row
    ] # square missing

ragged_data_2 = \
    [
        [
            [
                [0.95, 10, 10, 100, 100, 0.1],  # Box 1
                [0.90, 10, 20, 100, 100, 0.1]  # Box 2
            ],  # 1st square in the row
            [
                [0.85, 10, 10, 100, 100, 0.1],  # Box 1
                [0.85, 10, 20, 100, 100, 0.1]  # Box 2
            ]  # 2nd square in the row
        ],  # 1st row
        [
            [
                [0.95, 10, 10, 100, 100, 0.1],  # Box 1, missing Box 2
            ],  # 1st square in the row
            [
                [0.75, 10, 10, 100, 100, 0.8],  # Box 1
                [0.80, 10, 20, 100, 100, 0.8]  # Box 2
            ]  # 2nd square in the row
        ]  # 2nd row
    ] # box missing

ragged_data_3 = \
    [
        [
            [
                [0.95, 10, 10, 100, 100, 0.1],  # Box 1
                [0.90, 10, 20, 100, 100, 0.1]  # Box 2
            ],  # 1st square in the row
            [
                [0.85, 10, 10, 100, 100, 0.1],  # Box 1
                [0.85, 10, 20, 100, 100, 0.1]  # Box 2
            ]  # 2nd square in the row
        ],  # 1st row
        [
            [
                [0.95, 10, 10, 100, 100, 0.1],  # Box 1
                [0.90, 10, 20, 100, 100, 0.1]  # Box 2
            ],  # 1st square in the row
            [
                [0.75, 10, 10],  # Box 1, missing values
                [0.80, 10, 20, 100, 100, 0.8]  # Box 2
            ]  # 2nd square in the row
        ]  # 2nd row
    ] # values in a box missing

ragged_data_4 = \
    [
        [

            [0.95, 10, 10, 100, 100, 0.1],  # Box 1
            [0.90, 10, 20, 100, 100, 0.1],  # Box 2
            # 1st square in the row

            [0.85, 10, 10, 100, 100, 0.1],  # Box 1
            [0.85, 10, 20, 100, 100, 0.1]  # Box 2
            # 2nd square in the row
        ],  # 1st row
        [

            [0.95, 10, 10, 100, 100, 0.1],  # Box 1
            [0.90, 10, 20, 100, 100, 0.1],  # Box 2
            # 1st square in the row
            [0.75, 10, 10, 100, 100, 0.8],  # Box 1
            [0.80, 10, 20, 100, 100, 0.8]  # Box 2
            # 2nd square in the row
        ]  # 2nd row
    ] # 1 dimension missing

# Lists of categories of detectable objects
categories_1 = ["car", "motorcycle", "person"]
categories_2 = ["car", "motorcycle", "person", "traffic light"]
categories_3 = ["dog", "cat", "bird"]

# ******************* OUTPUT DATA *******************
# Outputs: output_n corresponding to input data_n; fn corresponding to specific function n
# Raw data n1
output_1_f1 = [[[0.76, 10, 10, 100, 100, 3], [0.68, 10, 10, 100, 100, 2], [0.16, 10, 20, 100, 100, 3]],
               [[0.76, 10, 10, 100, 100, 3], [0.64, 10, 20, 100, 100, 1], [0.04, 10, 10, 100, 100, 2]]]

output_1_f2 = [[[0.76, -40, -40, 60, 60, 3], [0.68, 360, -40, 460, 60, 2],
                [0.16, 760, -30, 860, 70, 3]],
               [[0.76, -40, 360, 60, 460, 3], [0.64, 360, 370, 460, 470, 1],
                [0.04, 760, 360, 860, 460, 2]]]

output_1_f3 = [[0.76, -40, -40, 60, 60, 3], [0.68, 360, -40, 460, 60, 2],
               [0.76, -40, 360, 60, 460, 3], [0.64, 360, 370, 460, 470, 1]]

output_1_f5 = [[0.76, -40, -40, 60, 60, 3], [0.68, 360, -40, 460, 60, 2],
               [0.76, -40, 360, 60, 460, 3], [0.64, 360, 370, 460, 470, 1]]

output_1 = ['Person detected with probability 0.76 at ((-40, -40), (60, 60))',
            'Motorcycle detected with probability 0.68 at ((360, -40), (460, 60))',
            'Person detected with probability 0.76 at ((-40, 360), (60, 460))',
            'Car detected with probability 0.64 at ((360, 370), (460, 470))']

# Raw data n2
output_2_f1 = [[[0.66, 120, 75, 100, 100, 3], [0.72, 70, 250, 100, 100, 1], [0.16, 200, 300, 100, 100, 4]],
               [[0.81, 190, 320, 100, 100, 4], [0.52, 390, 120, 100, 100, 1], [0.59, 10, 125, 100, 100, 2]]]

output_2_f2 = [[[0.66, 70, 25, 170, 125, 3], [0.72, 420, 200, 520, 300, 1],
                [0.16, 950, 250, 1050, 350, 4]],
               [[0.81, 140, 670, 240, 770, 4], [0.52, 740, 470, 840, 570, 1],
                [0.59, 760, 475, 860, 575, 2]]]

output_2_f3 = [[0.66, 70, 25, 170, 125, 3], [0.72, 420, 200, 520, 300, 1],
               [0.81, 140, 670, 240, 770, 4], [0.52, 740, 470, 840, 570, 1],
               [0.59, 760, 475, 860, 575, 2]]

output_2_f5 = [[0.66, 70, 25, 170, 125, 3], [0.72, 420, 200, 520, 300, 1],
               [0.81, 140, 670, 240, 770, 4], [0.59, 760, 475, 860, 575, 2]]

output_2 = ['Person detected with probability 0.66 at ((70, 25), (170, 125))',
            'Car detected with probability 0.72 at ((420, 200), (520, 300))',
            'Traffic light detected with probability 0.81 at ((140, 670), (240, 770))',
            'Motorcycle detected with probability 0.59 at ((760, 475), (860, 575))']

output_2_f3_bis = [[0.72, 420, 200, 520, 300, 1], [0.81, 140, 670, 240, 770, 4]]

output_2_f5_bis = [[0.66, 70, 25, 170, 125, 3], [0.72, 420, 200, 520, 300, 1],
                  [0.81, 140, 670, 240, 770, 4], [0.52, 740, 470, 840, 570, 1],
                  [0.59, 760, 475, 860, 575, 2]]

output_2_bis = ['Person detected with probability 0.66 at ((70, 25), (170, 125))',
                'Car detected with probability 0.72 at ((420, 200), (520, 300))',
                'Traffic light detected with probability 0.81 at ((140, 670), (240, 770))']

output_2_ter = ['Person detected with probability 0.66 at ((70, 25), (170, 125))',
                'Car detected with probability 0.72 at ((420, 200), (520, 300))',
                'Traffic light detected with probability 0.81 at ((140, 670), (240, 770))',
                'Car detected with probability 0.52 at ((740, 470), (840, 570))',
                'Motorcycle detected with probability 0.59 at ((760, 475), (860, 575))']

# Raw data n3
output_3_f1 = [[[0.72, 298, 70, 100, 20, 3], [0.68, 1, 70, 96, 20, 3], [0.56, 170, 298, 50, 50, 3]],
               [[0.12, 210, 170, 70, 70, 3], [0.72, 166, 80, 60, 50, 3], [0.56, 176, 2, 50, 50, 3]],
               [[0.12, 100, 110, 55, 80, 3], [0.64, 10, 20, 100, 100, 1], [0.51, 104, 260, 80, 80, 2]],
               [[0.76, 290, 10, 90, 90, 1], [0.04, 10, 10, 70, 70, 2], [0.48, 10, 220, 70, 70, 3]]]

output_3_f2 = [[[0.72, 248, 60, 348, 80, 3], [0.68, 253, 60, 349, 80, 3],
                [0.56, 745, 273, 795, 323, 3]],
               [[0.12, 175, 435, 245, 505, 3], [0.72, 436, 355, 496, 405, 3],
                [0.56, 751, 277, 801, 327, 3]],
               [[0.12, 72.5, 670, 127.5, 750, 3], [0.64, 260, 570, 360, 670, 1],
                [0.51, 664, 820, 744, 900, 2]],
               [[0.76, 245, 865, 335, 955, 1], [0.04, 275, 875, 345, 945, 2],
                [0.48, 575, 1085, 645, 1155, 3]]]

output_3_f3 = [[0.72, 248, 60, 348, 80, 3], [0.68, 253, 60, 349, 80, 3],
               [0.56, 745, 273, 795, 323, 3], [0.72, 436, 355, 496, 405, 3],
               [0.56, 751, 277, 801, 327, 3], [0.64, 260, 570, 360, 670, 1],
               [0.51, 664, 820, 744, 900, 2], [0.76, 245, 865, 335, 955, 1]]

output_3_f5 = [[0.72, 248, 60, 348, 80, 3], [0.56, 745, 273, 795, 323, 3],
               [0.72, 436, 355, 496, 405, 3], [0.64, 260, 570, 360, 670, 1],
               [0.51, 664, 820, 744, 900, 2], [0.76, 245, 865, 335, 955, 1]]

output_3 = ['Bird detected with probability 0.72 at ((248, 60), (348, 80))',
            'Bird detected with probability 0.56 at ((745, 273), (795, 323))',
            'Bird detected with probability 0.72 at ((436, 355), (496, 405))',
            'Dog detected with probability 0.64 at ((260, 570), (360, 670))',
            'Cat detected with probability 0.51 at ((664, 820), (744, 900))',
            'Dog detected with probability 0.76 at ((245, 865), (335, 955))']
