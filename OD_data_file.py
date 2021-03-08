# Object detection project, data file
photo_dim1 = [1200, 800]
photo_dim2 = [200, 800]

data1 = \
    [
        [
            [
                [0.95, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.90, 10, 20, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 1st square in the row
            [
                [0.85, 10, 10, 100, 100, 0.1, 0.8, 0.1], # Box 1
                [0.85, 10, 20, 100, 100, 0.1, 0.8, 0.1]  # Box 2
            ], # 2nd square in the row
            [
                [0.10, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.20, 10, 20, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 3rd square in the row
        ], # 1st row
        [
            [
                [0.95, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.90, 10, 20, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 1st square in the row
            [
                [0.75, 10, 10, 100, 100, 0.8, 0.1, 0.1], # Box 1
                [0.80, 10, 20, 100, 100, 0.8, 0.1, 0.1]  # Box 2
            ], # 2nd square in the row
            [
                [0.10, 10, 10, 100, 100, 0.2, 0.4, 0.4], # Box 1
                [0.00, 10, 20, 100, 100, 0.2, 0.4, 0.4]  # Box 2
            ] # 3rd square in the row
        ] # 2nd row
    ]

data2 = \
    [
        [
            [
                [0.95, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.90, 10, 20, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 1st square in the row
            [
                [0.85, 10, 10, 100, 100, 0.1, 0.8, 0.1], # Box 1
                [0.85, 10, 20, 100, 100, 0.1, 0.8, 0.1]  # Box 2
            ], # 2nd square in the row
            [
                [0.10, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.20, 10, 20, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 3rd square in the row
        ], # 1st row
        [
            [
                [0.95, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.90, 10, 20, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 1st square in the row
            [
                [0.75, 10, 10, 100, 100, 0.8, 0.1, 0.1], # Box 1
                [0.80, 10, 20, 100, 100, 0.8, 0.1, 0.1]  # Box 2
            ], # 2nd square in the row
            [
                [0.10, 10, 10, 100, 100, 0.2, 0.4, 0.4], # Box 1
                [0.00, 10, 20, 100, 100, 0.2, 0.4, 0.4]  # Box 2
            ] # 3rd square in the row
        ] # 2nd row
    ]

# missing a square
ragged_data_1 = \
    [
        [
            [
                [0.95, 10, 10, 100, 100, 0.1], # Box 1
                [0.90, 10, 20, 100, 100, 0.1]  # Box 2
            ] # 1st square in the row, missing 2nd square in the row
        ], # 1st row
        [
            [
                [0.95, 10, 10, 100, 100, 0.1], # Box 1
                [0.90, 10, 20, 100, 100, 0.1]  # Box 2
            ], # 1st square in the row
            [
                [0.75, 10, 10, 100, 100, 0.8], # Box 1
                [0.80, 10, 20, 100, 100, 0.8]  # Box 2
            ] # 2nd square in the row
        ] # 2nd row
    ]

# missing a box
ragged_data_2 = \
    [
        [
            [
                [0.95, 10, 10, 100, 100, 0.1], # Box 1
                [0.90, 10, 20, 100, 100, 0.1]  # Box 2
            ], # 1st square in the row
            [
                [0.85, 10, 10, 100, 100, 0.1], # Box 1
                [0.85, 10, 20, 100, 100, 0.1]  # Box 2
            ] # 2nd square in the row
        ], # 1st row
        [
            [
                [0.95, 10, 10, 100, 100, 0.1], # Box 1, missing Box 2
            ], # 1st square in the row
            [
                [0.75, 10, 10, 100, 100, 0.8], # Box 1
                [0.80, 10, 20, 100, 100, 0.8]  # Box 2
            ] # 2nd square in the row
        ] # 2nd row
    ]

# missing values in a box
ragged_data_3 = \
    [
        [
            [
                [0.95, 10, 10, 100, 100, 0.1], # Box 1
                [0.90, 10, 20, 100, 100, 0.1]  # Box 2
            ], # 1st square in the row
            [
                [0.85, 10, 10, 100, 100, 0.1], # Box 1
                [0.85, 10, 20, 100, 100, 0.1]  # Box 2
            ] # 2nd square in the row
        ], # 1st row
        [
            [
                [0.95, 10, 10, 100, 100, 0.1], # Box 1
                [0.90, 10, 20, 100, 100, 0.1]  # Box 2
            ], # 1st square in the row
            [
                [0.75, 10, 10], # Box 1, missing values
                [0.80, 10, 20, 100, 100, 0.8]  # Box 2
            ] # 2nd square in the row
        ] # 2nd row
    ]

# missing 1 dimension
ragged_data_4 = \
    [
        [

            [0.95, 10, 10, 100, 100, 0.1], # Box 1
            [0.90, 10, 20, 100, 100, 0.1], # Box 2
            # 1st square in the row

            [0.85, 10, 10, 100, 100, 0.1], # Box 1
            [0.85, 10, 20, 100, 100, 0.1]  # Box 2
            # 2nd square in the row
        ], # 1st row
        [

            [0.95, 10, 10, 100, 100, 0.1], # Box 1
            [0.90, 10, 20, 100, 100, 0.1], # Box 2
            # 1st square in the row
            [0.75, 10, 10, 100, 100, 0.8], # Box 1
            [0.80, 10, 20, 100, 100, 0.8]  # Box 2
            # 2nd square in the row
        ] # 2nd row
    ] # missing 1 dimension

categories1 = ["car", "motorcycle", "person"]
categories2 = ["car", "motorcycle", "person", "traffic light"]

IoU_threshold1 = 0.5

filtering_threshold1 = 0.5
