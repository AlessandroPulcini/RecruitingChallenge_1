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
        4-tuple containing the value of the 4 dimensions of the data_ list
    """

    # check for a correct dimension of the matrix
    try:
        par_Bp = len(data_)
        par_Ap = len(data_[0])
        par_M = len(data_[0][0])
        par_K = len(data_[0][0][0]) - 5
    except IndexError:
        print("Data structure has not the correct dimension")
        raise ValueError

    # check the whole data matrix for rugs
    for Ap_element in data_:
        if len(Ap_element) != par_Ap:
            print("Data matrix is ragged")
            raise ValueError
        for M_element in Ap_element:
            if len(M_element) != par_M:
                print("Data matrix is ragged")
                raise ValueError
            for K_element in M_element:
                if len(K_element) != (par_K + 5):
                    print("Data matrix is ragged")
                    raise ValueError

    # check for consistency on the K parameter
    if par_K != len(categories_):
        print("K parameter is inconsistent")
        raise ValueError

    # check for consistency on N
    if photo_dim_[0] / par_Ap != photo_dim_[1] / par_Bp:
        print("Photo dimensions are inconsistent with data structure")
        raise ValueError

    return par_Bp, par_Ap, par_M, par_K


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
        for element in data_[B][A]:
            for i, x in enumerate(element[5:]):
                if (element[0] * x) > probability:
                    probability = element[0] * x
                    index = i
                    box = element
        data_[B][A] = [probability] + box[1:5] + [index + 1]
    return data_


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
        IoU_value = 0
    else:
        I_area = (x_max - x_min) * (y_max - y_min)
        U_area = (box1[3] - box1[1]) * (box1[4] - box1[2]) + \
                 (box2[3] - box2[1]) * (box2[4] - box2[2]) - \
                 I_area
        IoU_value = I_area / U_area

    return IoU_value


def suppression(data_, suppr_ = 0.5):
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
