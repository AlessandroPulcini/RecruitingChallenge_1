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
    for Bp, Ap in itertools.product(range(len(data_)), range(len(data_[0]))):
        probability = 0
        for element in data_[Bp][Ap]:
            for i, x in enumerate(element[5:]):
                if (element[0] * x) > probability:
                    probability = element[0] * x
                    index = i
                    box = element
        data_[Bp][Ap] = [probability] + box[1:5] + [index + 1]
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
    for Bp, Ap in itertools.product(range(len(data_)), range(len(data_[0]))):
        data_[Bp][Ap] = [data_[Bp][Ap][0]] + \
                        [Ap * N_size + data_[Bp][Ap][1] - data_[Bp][Ap][3] / 2] + \
                        [Bp * N_size + data_[Bp][Ap][2] - data_[Bp][Ap][4] / 2] + \
                        [Ap * N_size + data_[Bp][Ap][1] + data_[Bp][Ap][3] / 2] + \
                        [Bp * N_size + data_[Bp][Ap][2] + data_[Bp][Ap][4] / 2] + \
                        [data_[Bp][Ap][-1]]
    return data_


def filtering(data_, thrsh_=0.5):
    """

    Parameters:
        data_: The 3-dimensional list containing information about one box per square and coordinated expressed
            in format 2
        thrsh_: Threshold parameter with default value of 0.5
    Return:
        A subset of input boxes containing only those with probability greater than or equal to the threshold
    """
    filtered_data = []
    for Bp, Ap in itertools.product(range(len(data_)), range(len(data_[0]))):
        if data_[Bp][Ap][0] >= thrsh_:
            filtered_data.append(data_[Bp][Ap])
    return filtered_data
