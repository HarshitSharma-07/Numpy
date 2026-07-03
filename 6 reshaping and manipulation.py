#RESHAPING
# dimensions must be same
# reshaping does not create a new array, instead it gives us a view

import numpy as np
arr=np.array([1,2,3,4,5,6])
reshaped_Arr=arr.reshape(3,2)
print(reshaped_Arr)


#FLATTENING AND RAVELING
# to convert multidimensional array into 1 dimensional
# ravel->creates a view
# flatten->creates an actual copy of the array


arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.ravel())
flattened_arr=arr.flatten()
print(flattened_arr)