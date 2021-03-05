import libs
from data_file import photo_dim, data, categories

try:
    from data_file import IoU_threshold, filtering_threshold
except ImportError:
    IoU_threshold = 0.5
    filtering_threshold = 0.5

# checking data structure for anomalies and read data dimensions
(par_Bp, par_Ap, par_M, par_K) = libs.data_structure_check(data, photo_dim, categories)

# creating a dictionary for categories
cat_dict = {}
for ind, cat in enumerate(categories):
    cat_dict[ind + 1] = cat

# Step 1.a: class determination
data = libs.determine_class(data)
# Step 1.b: coordinates conversion
data = libs.coordinate_conversion(data, photo_dim[0] / par_Ap)
#print(data)

# Step 2: filtering
filtered_subset = libs.filtering(data, filtering_threshold)
#print(filtered_subset)

# Step 3: Non-max suppression
filtered_subset = libs.suppression(filtered_subset, IoU_threshold)

# Output: List of string stating category detected with given probability (.2f) at location (in format 2)
output_list = []
for box in filtered_subset:
    output_str = cat_dict[box[-1]].capitalize() + \
                 " detected with probability " + \
                 "{0:.2f}".format(box[0]) + \
                 " at ((" + str(box[1]) + ", " + str(box[2]) + "), (" + \
                 str(box[3]) + ", " + str(box[4]) + "))"
    output_list.append(output_str)

print(output_list)
