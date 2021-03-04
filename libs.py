def data_structure_check(data_, photo_dim_, categories_):

    par_Bp = 0
    par_Ap = 0
    par_M  = 0
    par_K  = 0

    # check for a correct dimension of the matrix
    try:
        par_Bp = len(data_)
        par_Ap = len(data_[0])
        par_M = len(data_[0][0])
        par_K = len(data_[0][0][0]) - 5
    except IndexError:
        exit("Data dimension error")

    # check the whole data matrix for rugs
    for Ap_element in data_:
        if len(Ap_element) != par_Ap:
            exit("Ragged matrix on A")
        for M_element in Ap_element:
            if len(M_element) != par_M:
                exit("Ragged matrix on M")
            for K_element in M_element:
                if (len(K_element) - 5) != par_K:
                    exit("Ragged matrix on K")

    # check for consistency on the K parameter
    if par_K != len(categories_):
        exit("K error")

    # check for consistency on N
    if photo_dim_[0] / par_Ap != photo_dim_[1] / par_Bp:
        exit("A/B error")

    return (par_Bp, par_Ap, par_M, par_K)
