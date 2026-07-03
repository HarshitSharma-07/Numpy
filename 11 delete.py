import numpy as np
# creates new array, original one remains intact

arr=np.array([1,2,3,4,5,6,7])
new_array=np.delete(arr,6)
print(new_array)

# Now for 2d array

arr_2d=np.array([[1,2,3],[4,5,6]])
new_2d_arr=np.delete(arr_2d,1,axis=0)
print(new_2d_arr)