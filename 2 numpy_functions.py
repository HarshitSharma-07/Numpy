import numpy as np

array_2d=np.array([[1,2,3],[4,5,6]])
print(array_2d)
print(array_2d.shape)   #returns no of rows and columns
print(array_2d.size)    #returns no of elements in matrix

array1=np.array([1,2,3,4])
array2=np.array([[1,2,3],[4,5,6]])
array3=np.array([[[1,2],[3,4],[5,6],[7,8]],[[0,1],[2,3],[4,5],[6,7]]])
print(array1.ndim)
print(array2.ndim)
print(array3.ndim)
#returns no. of dimension of the array 


non_homogeneous_array=np.array([1,2,3,4,5,"hello"])
print(non_homogeneous_array.dtype)





array=np.array([1,2,3,4,5])
float_conversion=array.astype(str)
print(float_conversion)





arr = np.array([[1, 2],
                [3, 4]])

print(arr.sum(axis=0))
print(arr.sum(axis=1))