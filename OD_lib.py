# Object detection project, library
import itertools


def data_structure_check(data_, photo_dim_, categories_):
    """
    Parameters:
        data_: the 4-dimensional list containing the raw output
        photo_dim_: original photo dimensions
        categories_: list of category names
    Method:
        check for consistency in the data structure
    Return:
        square size N
    """

    # check for a correct dimension of the matrix
    try:
        par_Bp = len(data_)
        par_Ap = len(data_[0])
        par_M = len(data_[0][0])
        par_K = len(data_[0][0][0]) - 5
    except (IndexError, TypeError):
        print("Data structure has not the correct dimension")
        raise ValueError

    # check the whole data matrix for rugs
    for Ap_element in data_:
        if len(Ap_element) != par_Ap:
            print("Data matrix is ragged on rows")
            raise ValueError
        for M_element in Ap_element:
            if len(M_element) != par_M:
                print("Data matrix is ragged on squares")
                raise ValueError
            for K_element in M_element:
                if len(K_element) != (par_K + 5):
                    print("Data matrix is ragged on boxes")
                    raise ValueError

    # check for consistency on the K parameter
    if par_K != len(categories_):
        print("K parameter is inconsistent")
        raise ValueError

    # check for consistency on N
    if photo_dim_[0] / par_Ap != photo_dim_[1] / par_Bp:
        print("Photo dimensions are inconsistent with data structure")
        raise ValueError

    return photo_dim_[0] / par_Ap


def create_dict(categories_):
    cat_dict_ = {}
    for ind, cat in enumerate(categories_):
        cat_dict_[ind + 1] = cat
    return cat_dict_


# Step 1: function 1
def determine_class(data_):
    """
    Parameters:
        data_: the 4-dimensional list containing the raw output
    Return:
        A 3-dimensional list with the probability, for each NxN square, of containing an object of a specific category
            (chosen as the one giving the highest probability)
    """
    for B, A in itertools.product(range(len(data_)), range(len(data_[0]))):
        probability = 0
        box = []
        index = 0
        for element in data_[B][A]:
            for i, x in enumerate(element[5:]):
                if (element[0] * x) > probability:
                    probability = element[0] * x
                    index = i
                    box = element
        if not box:
            box = data_[B][A][0]
            # if -for any reason- there is a square with only boxes of probability = 0, this allows the correct
            # functioning of the code
        data_[B][A] = [round(probability, 2)] + box[1:5] + [index + 1]
    return data_


# Step 1: function 2
def coordinate_conversion(data_, N_size):
    """
    Parameters:
        data_: The 3-dimensional list containing information about one box per square and coordinated expressed
            in format 1
        N_size: Size of a single square N
    Return:
        A 3-dimensional list like the parameter "data_" with coordinates converted in format 2
    """
    for B, A in itertools.product(range(len(data_)), range(len(data_[0]))):
        data_[B][A] = [data_[B][A][0]] + \
                      [A * N_size + data_[B][A][1] - data_[B][A][3] / 2] + \
                      [B * N_size + data_[B][A][2] - data_[B][A][4] / 2] + \
                      [A * N_size + data_[B][A][1] + data_[B][A][3] / 2] + \
                      [B * N_size + data_[B][A][2] + data_[B][A][4] / 2] + \
                      [data_[B][A][-1]]
    return data_


# Step 2: function 3
def filtering(data_, thrsh_=0.5):
    """
    Parameters:
        data_: The 3-dimensional list containing information about one box per square and coordinated expressed
            in format 2
        thrsh_: Threshold parameter with default value of 0.5
    Return:
        A subset of input boxes in form of a 2-dimensional array containing only those with probability greater
        than or equal to the threshold
    """
    filtered_data = []
    for B, A in itertools.product(range(len(data_)), range(len(data_[0]))):
        if data_[B][A][0] >= thrsh_:
            filtered_data.append(data_[B][A])
    return filtered_data


# Step 3: function 4
def IoU_calculation(box1, box2):
    """
    Parameters:
        box1: List of parameter describing a single box with format 2
        box2: List of parameter describing a single box with format 2
    Return:
        Intersection over union of the two rectangles
    """

    x_min = max(box1[1], box2[1])
    y_min = max(box1[2], box2[2])
    x_max = min(box1[3], box2[3])
    y_max = min(box1[4], box2[4])
    if (x_min > x_max) or (y_min > y_max):
        return 0
    else:
        I_area = (x_max - x_min) * (y_max - y_min)
        U_area = (box1[3] - box1[1]) * (box1[4] - box1[2]) + \
                 (box2[3] - box2[1]) * (box2[4] - box2[2]) + \
                 - I_area

    return I_area / U_area


# Step 3: function 5
def suppression(data_, suppr_=0.5):
    """
    Parameters:
        data_: The 3-dimensional list containing information about one box per square and coordinated expressed
            in format 2
        suppr_: Threshold parameter with default value of 0.5
    Return:
        A subset of input boxes without overlapping boxes
    """
    for el1 in data_:
        for el2 in data_:
            if IoU_calculation(el1, el2) > suppr_:
                if el1[0] > el2[0]:
                    data_.remove(el2)
                else:
                    data_.remove(el1)
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
                     " at ((" + str(box[1]) + ", " + str(box[2]) + "), (" + \
                     str(box[3]) + ", " + str(box[4]) + "))"
        output_list.append(output_str)
    return output_list


# Function 6
def main(photo_dim, data, categories, IoU_threshold=0.5, filtering_threshold=0.5):
    # checking data structure for anomalies and read data dimensions
    N_size = data_structure_check(data, photo_dim, categories)

    # creating a dictionary for categories
    cat_dict = create_dict(categories)

    # Step 1.a: class determination
    data = determine_class(data)
    # Step 1.b: coordinates conversion
    data = coordinate_conversion(data, N_size)

    # Step 2: filtering
    data = filtering(data, filtering_threshold)

    # Step 3: Non-max suppression
    data = suppression(data, IoU_threshold)

    # Output: List of string stating category detected with given probability (.2f) at location (in format 2)
    output_list = print_data(data, cat_dict)

    return output_list
