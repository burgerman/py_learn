import numpy as np
x = np.array([1, np.nan, 5, 9], dtype=float)
print("Original Arr: \n", x)
median_x = np.nanmean(x)

# Get the indices where values are NaN
nan_indices = np.isnan(x)
# Replace NaNs with median val
x[nan_indices] = median_x
print("Cleansed Arr: \n", x)