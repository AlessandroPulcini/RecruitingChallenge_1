# Object detection project, library
import itertools
import numpy as np
from copy import deepcopy


def data_structure_check(data_, photo_dim_, categories_):
    """
    Parameters:
        data_: the 4-dimensional list containing the raw data
        photo_dim_: original photo dimensions
        categories_: list of category names
    Method:
        check for consistency in the data structure
    Return:
        square size N
    """
    # check for the correct format of the matrix
    if np.ndim(np.array(data_, dtype=object)) != 4:
        raise ValueError("Data structure has not the correct format")
    (par_Bp, par_Ap, par_M, par_K) = np.shape(data_)
    par_K -= 5

    # check for consistency on the K parameter
    if par_K != len(categories_):
        raise ValueError("K parameter is inconsistent")

    # check for consistency on N
    if photo_dim_[0] / photo_dim_[1] != par_Ap / par_Bp:
        raise ValueError("Photo dimensions are inconsistent with data structure")

    return photo_dim_[0] / par_Ap


def create_dict(categories_):
    cat_dict = {}
    for ind, cat in enumerate(categories_):
        cat_dict[ind + 1] = cat
    return cat_dict


# Step 1: function 1
def determine_class(data_):
    """
    Parameters:
        data_: the 4-dimensional list containing the raw data
    Return:
        A 3-dimensional list with the probability, for each NxN square, of containing an object of a specific category
            (chosen as the one giving the highest probability)
    """
    (par_Bp, par_Ap, par_M, par_K) = np.shape(data_)
    for b, a in itertools.product(range(par_Bp), range(par_Ap)):
        probability = 0
        box = []
        index = 0
        for element in data_[b][a]:
            for i, x in enumerate(element[5:]):
                if (element[0] * x) > probability:
                    probability = element[0] * x
                    index = i
                    box = element
        if not box:
            box = data_[b][a][0]
            # if -for any reason- there is a square with only boxes of probability = 0, this allows the correct
            #   functioning of the code
        data_[b][a] = [round(probability, 2)] + box[1:5] + [index + 1]
    return data_


# Step 1: function 2
def coordinates_conversion(data_, n_size_):
    """
    Parameters:
        data_: The 3-dimensional list containing information about one box per square and coordinated expressed
            in format 1
        n_size_: Size of a single square N
    Return:
        A 3-dimensional list like the input parameter "data_" with coordinates converted in format 2
    """
    (par_Bp, par_Ap, dummy) = np.shape(data_)
    for b, a in itertools.product(range(par_Bp), range(par_Ap)):
        data_[b][a] = [data_[b][a][0]] + \
                      [a * n_size_ + data_[b][a][1] - data_[b][a][3] / 2] + \
                      [b * n_size_ + data_[b][a][2] - data_[b][a][4] / 2] + \
                      [a * n_size_ + data_[b][a][1] + data_[b][a][3] / 2] + \
                      [b * n_size_ + data_[b][a][2] + data_[b][a][4] / 2] + \
                      [data_[b][a][-1]]
    return data_


# Step 2: function 3
def filtering(data_, thresh_=0.5):
    """
    Parameters:
        data_: The 3-dimensional list containing information about one box per square and coordinated expressed
            in format 2
        thresh_: Threshold parameter with default value of 0.5
    Return:
        A subset of input boxes in form of a 2-dimensional array containing only those with probability greater
        than or equal the threshold
    """
    filtered_data = []
    (par_Bp, par_Ap, par_K) = np.shape(data_)
    for element in np.reshape(data_, (par_Bp*par_Ap, par_K)):
        if element[0] >= thresh_:
            filtered_data.append(element.tolist())
    return filtered_data


# Step 3: function 4
def iou_calculation(box1_, box2_):
    """
    Parameters:
        box1_: List of parameter describing a single box in format 2
        box2_: List of parameter describing a single box in format 2
    Return:
        Intersection-over-union value of the two rectangles
    """
    x_min = max(box1_[1], box2_[1])
    y_min = max(box1_[2], box2_[2])
    x_max = min(box1_[3], box2_[3])
    y_max = min(box1_[4], box2_[4])
    if (x_min > x_max) or (y_min > y_max):
        return 0
    else:
        i_area = (x_max - x_min) * (y_max - y_min)
        u_area = (box1_[3] - box1_[1]) * (box1_[4] - box1_[2]) + \
                 (box2_[3] - box2_[1]) * (box2_[4] - box2_[2]) + \
                 - i_area
    return i_area / u_area


# Step 3: function 5
def non_max_suppression(data_, thresh_=0.5):
    """
    Parameters:
        data_: The 3-dimensional list containing information about one box per square and coordinated expressed
            in format 2
        thresh_: Intersection-over-union threshold parameter with default value of 0.5
    Return:
        A subset of input boxes in form of a 2-dimensional array without overlapping boxes. Two boxes are considered
        to be overlapping if their intersection-over-union value is higher than thrsh_ input parameter
    """
    sorted_data = sorted(data_, reverse=True, key=lambda x: x[0])
    for index, el1 in enumerate(sorted_data):
        if el1 in data_:
            for el2 in sorted_data[index+1:]:
                if el2 in data_ and iou_calculation(el1, el2) > thresh_:
                    data_.remove(el2)
    return data_


def print_data(data_, cat_dict_):
    """
    Parameters:
        data_: The 3-dimensional list containing information about one box per square and coordinated expressed
            in format 2
        cat_dict_: Dictionary of categories of detectable items
    Return:
        A list of strings containing information about each detected item, their category and position
    """
    output_list = []
    for box in data_:
        output_str = cat_dict_[box[-1]].capitalize() + \
                     " detected with probability " + \
                     "{0:.2f}".format(box[0]) + \
                     " at ((" + str(int(box[1])) + ", " + str(int(box[2])) + "), " +\
                     "(" + str(int(box[3])) + ", " + str(int(box[4])) + "))"
        output_list.append(output_str)
    return output_list


# Function 6
def object_detection(photo_dim, original_data, categories, iou_threshold=0.5, filtering_threshold=0.5):
    """
    Parameters:
        photo_dim: Original photo dimensions
        original_data: A 4-dimensional list containing the raw data, will not be modified
        categories: List of categories of detectable objects
        iou_threshold: Intersection over union threshold value, with default value of 0.5
        filtering_threshold: Filtering threshold value, with default value of 0.5
    Return:
        A list of strings containing information about each detected item, their category and position
    """

    # creating a copy to left original_data unmodified
    data = deepcopy(original_data)

    # checking data structure for anomalies and read data dimensions
    n_size = data_structure_check(data, photo_dim, categories)

    # creating a dictionary for categories
    cat_dict = create_dict(categories)

    # Step 1.a: class determination
    data = determine_class(data)
    # Step 1.b: coordinates conversion
    data = coordinates_conversion(data, n_size)

    # Step 2: filtering
    data = filtering(data, filtering_threshold)

    # Step 3: Non-max suppression
    data = non_max_suppression(data, iou_threshold)

    # Output: List of string stating category detected with given probability (.2f) at location (in format 2)
    output_list = print_data(data, cat_dict)

    return output_list
