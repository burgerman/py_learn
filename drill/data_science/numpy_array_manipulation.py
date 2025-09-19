import numpy as np

# Array
arr = np.array([1, 2, 3, 4, 5], ndmin=2)
print(arr)
print(arr[0, 1:5:2]) # start index 1, end index(exclusive) 5, step to move 2
# [2, 4]

print("the number of dimensions: {}".format(arr.ndim))
print(f"First arr, head element: {arr[0, : 1]}")
print("First arr, tail element: %s" % (arr[0, -1:]))

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], ndmin=3)
#shape
print("array shape: ",arr2.shape) # (1, 2, 5)
print(arr2[0, 0:2, 1:4])
# [[2 3 4]
# [7 8 9]]

arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
# transpose
print("transpose:\n", arr3.T)

# Data type
newarr = arr.astype('f')
print(newarr)
print(newarr.dtype)
for e in newarr[0]:
    # print(f"{e}")
    print("{:.1f}".format(e))

# copy (new data) vs view (doesn't own data)
cp = arr.copy()
vw = arr.view()

print("copy base: ", cp.base) # None
print("view base: ", vw.base) # arr: [1 2 3 4 5]


# Array Reshape (based on a view)
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"{arr_1d}")
print("original shape", arr_1d.shape)
print("original num of dimensions",arr_1d.ndim)
reshaped_arr_2d = arr_1d.reshape(4, 3)
print(f"{reshaped_arr_2d}")
print("shape after reshape: ", reshaped_arr_2d.shape)
print("num of dimensions after reshape: ", reshaped_arr_2d.ndim)
reshaped_arr_3d = arr_1d.reshape(2, 3, 2)
print(f"{reshaped_arr_3d}")
print("shape after reshape: ", reshaped_arr_3d.shape)
print("num of dimensions after reshape: ", reshaped_arr_3d.ndim)
print(f"reshape base: {reshaped_arr_3d.base}")

# Unknown Dimension
unknown_dim_arr_3d = arr_1d.reshape(2, 2, -1)
print("Unknown Dimension Array: ")
print(unknown_dim_arr_3d)
# Flatten the array
flattened_arr_1d = arr2.reshape(-1)
print("Flattened Array: ", flattened_arr_1d)
print("Base Array: ", flattened_arr_1d.base)

# array split
split_arr_1d = np.array_split(arr_1d, 4)
print("split 1D array: ", split_arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
split_arr_2d = np.array_split(arr_2d, 3)
print("split 2D array along rows: ", split_arr_2d)

# Split along columns
# col_split_arr_2d = np.array_split(arr_2d, 3, axis=1)
col_split_arr_2d = np.hsplit(arr_2d, 3)
print("split 2D array along columns: ", col_split_arr_2d)


# concatenate arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr_concat = np.concatenate((arr1, arr2))
# arr_concat = np.hstack((arr1, arr2))
print("concatenated array: ", arr_concat)
# 1-D column-based concatenation
arr_col_concat = np.stack([arr1, arr2], axis=1)
print("concatenated col-based array: ", arr_col_concat)

# column-based concatenation
arr1_2d = np.array([[1, 2], [3, 4]])
arr2_2d = np.array([[5, 6], [7, 8]])
arr_concat_2d = np.concatenate((arr1_2d, arr2_2d), axis=1)
print("concatenated array 2D: ", arr_concat_2d)

# Search in the array
target_1d = np.where(arr_1d % 2 == 0)
print(target_1d)

# find the indices where the target element should be inserted in the sorted array
target_index = np.searchsorted(arr_1d, 5, side="left")
print(target_index)

# sort array
unsorted_arr_2d = np.array([[3, 2, 4], [5, 0, 1]])
print("Indices of Sorted 2D array: ", np.argsort(unsorted_arr_2d)) # returns the indices of elements within the original arr in the order of sorted array
print("Sorted 2D array: ", np.sort(unsorted_arr_2d)) # returns sorted copy

# filtering
custom_filter = arr_1d > 5
filtered_arr = arr_1d[custom_filter]
print("filtered array: ", filtered_arr)

# Rolling array, +1: shift element to the right by 1, -1: shift element to the left by 1 along columns
rolled_col_arr = np.roll(arr_2d, -1, axis=1)
print("col-based rolled array: ", rolled_col_arr)

rolled_row_arr = np.roll(arr_2d, 1, axis=0)
print("row-based rolled array: ", rolled_row_arr)