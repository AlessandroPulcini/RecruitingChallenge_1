photo_dim = [1200, 800]

data = \
    [
        [
            [
                [0.95, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.90, 10, 10, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 1st square in the row
            [
                [0.85, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.80, 10, 10, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 2nd square in the row
            [
                [0.10, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.00, 10, 10, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 3rd square in the row
        ], # 1st row
        [
            [
                [0.95, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.90, 10, 10, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 1st square in the row
            [
                [0.85, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.80, 10, 10, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 2nd square in the row
            [
                [0.10, 10, 10, 100, 100, 0.1, 0.1, 0.8], # Box 1
                [0.00, 10, 10, 100, 100, 0.1, 0.1, 0.8]  # Box 2
            ], # 3rd square in the row
        ] # 2nd row
    ]

categories = ["car", "motorcycle", "person"]

IoU_threshold = 0.5

filtering_threshold = 1