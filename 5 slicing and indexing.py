# exactly same as lists

import numpy as np
arr=np.array([1,2,3,4,5,6,7])
arr_2d=np.array([[1,2,3],[4,500,6]])
print(arr_2d[1,1])
print(arr_2d[1][1])
print(arr[1])
print(arr[2])

print(arr[0:6])
print(arr[2:7:2])
print(arr[::-1])


# how to print complete rows and columns in a 2d array

print("sliced row: ",arr_2d[2])
print("sliced column: ",arr_2d[:,2])  #[:,x] ":" means that i want to print all the rows 



# fancy indexing
# getting multiple elements at once

print(arr[[0,4,6]])#pass the indices in form of list