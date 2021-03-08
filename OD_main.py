# Object detection project, main program
from OD_lib import *
from OD_data_file import *


# checking data structure for anomalies and read data dimensions
N_size = data_structure_check(data1, photo_dim1, categories1)
print("N par:    {0:.0f}".format(N_size))

# creating a dictionary for categories
cat_dict = create_dict(categories1)
print("Dict:     {}".format(cat_dict))

# Step 1.a: class determination
data1 = determine_class(data1)
print("Step1.a: ", data1)
# Step 1.b: coordinates conversion
data1 = coordinate_conversion(data1, N_size)
print("Step1.b: ",data1)

# Step 2: filtering
data1 = filtering(data1, filtering_threshold1)
print("Step2:   ",data1)

# Step 3: Non-max suppression
data1 = suppression(data1, IoU_threshold1)
print("Step3:   ",data1)

# Output: List of string stating category detected with given probability (.2f) at location (in format 2)
output_list = print_data(data1, cat_dict)
print("Step4:   ",output_list)
