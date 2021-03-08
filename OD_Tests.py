# Object detection project, test program
from OD_lib import *
from OD_data_file import *
import pytest
import unittest


class BaseTests(unittest.TestCase):

    # Test function 6
    def test_main(self):
        self.assertEqual(['Motorcycle detected with probability 0.68 at ((360.0, -40.0), (460.0, 60.0))',
                          'Car detected with probability 0.64 at ((360.0, 370.0), (460.0, 470.0))'],
                         main(photo_dim1, data1, categories1, IoU_threshold1, filtering_threshold1))

    # Test errors
    def test_errors(selfself):
        with pytest.raises(ValueError):
            data_structure_check(ragged_data_1, photo_dim1, categories1)

        with pytest.raises(ValueError):
            data_structure_check(ragged_data_2, photo_dim1, categories1)

        with pytest.raises(ValueError):
            data_structure_check(ragged_data_3, photo_dim1, categories1)

        with pytest.raises(ValueError):
            data_structure_check(ragged_data_4, photo_dim1, categories1)

        with pytest.raises(ValueError):
            data_structure_check(data1, photo_dim1, categories2)

        with pytest.raises(ValueError):
            data_structure_check(data1, photo_dim2, categories1)


if __name__ == '__main__':
    unittest.main()
