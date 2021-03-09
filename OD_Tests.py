# Object detection project, test program
from OD_lib import *
from OD_data_file import *
import pytest
import unittest
from copy import deepcopy


# All data items for tests (input matrices; output matrices, lists, and strings) are stored in "OD_data_file"
#       for readability reasons.
# Input data are cloned before each test as the functions modifies the input data making them unusable
#       for further tests, except for the "object_detection" function, that clones the input data by itself.
class BaseTests(unittest.TestCase):

    # Test function 1
    def test_determine_class(self):
        input_data = deepcopy(data_1)
        self.assertEqual(output_1_f1, determine_class(input_data))
        input_data = deepcopy(data_2)
        self.assertEqual(output_2_f1, determine_class(input_data))
        input_data = deepcopy(data_3)
        self.assertEqual(output_3_f1, determine_class(input_data))

    # Test function 2
    def test_coordinate_conversion(self):
        input_data = deepcopy(output_1_f1)
        self.assertEqual(output_1_f2, coordinates_conversion(input_data, 400))
        input_data = deepcopy(output_2_f1)
        self.assertEqual(output_2_f2, coordinates_conversion(input_data, 400))
        input_data = deepcopy(output_3_f1)
        self.assertEqual(output_3_f2, coordinates_conversion(input_data, 300))

    # Test function 3
    def test_filtering(self):
        input_data = deepcopy(output_1_f2)
        self.assertEqual(output_1_f3, filtering(input_data))
        input_data = deepcopy(output_2_f2)
        self.assertEqual(output_2_f3, filtering(input_data))
        input_data = deepcopy(output_2_f2)
        self.assertEqual(output_2_f3_bis, filtering(input_data, 0.7))
        input_data = deepcopy(output_3_f2)
        self.assertEqual(output_3_f3, filtering(input_data))

    # Test function 4
    def test_IoU_calculation(self):
        self.assertEqual(0, IoU_calculation([1, 70, 25, 170, 125, 3], [1, 420, 25, 520, 125, 1]))
        self.assertEqual(0, IoU_calculation([1, 70, 25, 170, 125, 3], [1, 25, 225, 170, 325, 1]))
        self.assertEqual(0, IoU_calculation([1, 50, 50, 150, 150, 3], [1, 200, 200, 300, 300, 1]))
        self.assertEqual(1, IoU_calculation([1, 75, 25, 175, 125, 3], [1, 75, 25, 175, 125, 3]))
        self.assertEqual(0.5, IoU_calculation([1, 0, 0, 300, 300, 3], [1, 0, 100, 300, 400, 3]))
        self.assertEqual(1/3, IoU_calculation([1, 0, 0, 500, 200, 3], [1, 0, 100, 500, 300, 3]))

    # Test function 5
    def test_suppression(self):
        input_data = deepcopy(output_1_f3)
        self.assertEqual(output_1_f5, non_max_suppression(input_data))
        input_data = deepcopy(output_2_f3)
        self.assertEqual(output_2_f5, non_max_suppression(input_data))
        input_data = deepcopy(output_2_f3)
        self.assertEqual(output_2_f5_bis, non_max_suppression(input_data, 0.65))
        input_data = deepcopy(output_3_f3)
        self.assertEqual(output_3_f5, non_max_suppression(input_data))

    # Test function 6
    def test_main(self):
        self.assertEqual(output_1, object_detection(photo_dim_1, data_1, categories_1, 0.5, 0.5))
        self.assertEqual(output_2, object_detection(photo_dim_1, data_2, categories_2))
        self.assertEqual(output_2_bis, object_detection(photo_dim_2, data_2, categories_2, 0.5, 0.6))
        self.assertEqual(output_2_ter, object_detection(photo_dim_2, data_2, categories_2, 0.65))
        self.assertEqual(output_3, object_detection(photo_dim_3, data_3, categories_3))

    # Test errors
    def test_errors(self):
        # square missing in raw data
        with pytest.raises(ValueError):
            data_structure_check(ragged_data_1, photo_dim_1, categories_1)
        # box missing in raw data
        with pytest.raises(ValueError):
            data_structure_check(ragged_data_2, photo_dim_1, categories_1)
        # values in a box missing in raw data
        with pytest.raises(ValueError):
            data_structure_check(ragged_data_3, photo_dim_1, categories_1)
        # 1 dimension missing in raw data structure
        with pytest.raises(ValueError):
            data_structure_check(ragged_data_4, photo_dim_1, categories_1)
        # category number mismatching
        with pytest.raises(ValueError):
            data_structure_check(data_1, photo_dim_1, categories_2)
        # photo dimension mismatching
        with pytest.raises(ValueError):
            data_structure_check(data_1, photo_dim_error_test, categories_1)


if __name__ == '__main__':
    unittest.main()
