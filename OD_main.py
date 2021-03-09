# Object detection project, main program
from OD_lib import *
from OD_data_file import *
from copy import deepcopy


data = deepcopy(data_1)
cat = categories_1
photo_dim = photo_dim_1
print("Input:   ", data)
IoU_threshold = 0.5
filtering_threshold = 0.5

# checking data structure for anomalies and read data dimensions
N_size = data_structure_check(data, photo_dim, cat)
print("N par:    {0:.0f}".format(N_size))

# creating a dictionary for categories
cat_dict = create_dict(cat)
print("Dict:     {}".format(cat_dict))

# Step 1.a: class determination
data = determine_class(data)
print("Step1.a: ", data)

# Step 1.b: coordinates conversion
data = coordinates_conversion(data, N_size)
print("Step1.b: ",data)

# Step 2: filtering
data = filtering(data, filtering_threshold)
print("Step2:   ",data)

# Step 3: Non-max suppression
data = non_max_suppression(data, IoU_threshold)
print("Step3:   ",data)

# Output: List of string stating category detected with given probability (.2f) at location (in format 2)
output_list = print_data(data, cat_dict)
print("Step4:   ",output_list)
