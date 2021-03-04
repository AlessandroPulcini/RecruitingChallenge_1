import libs
from data_file import photo_dim, data, categories
try:
    from data_file import IoU_threshold, filtering_threshold
except ImportError:
    IoU_threshold = 0
    filtering_threshold = 0

# checking data structure for anomalies
(par_Bp, par_Ap, par_M, par_K) = libs.data_structure_check(data, photo_dim, categories)

# creating dictionary
cat_dict = {}
for ind, cat in enumerate(categories):
    cat_dict[cat] = ind

print(IoU_threshold)