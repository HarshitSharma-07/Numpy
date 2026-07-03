import numpy as np
# axis=0 for horizontal stacking
# axis=1 for vertical stacking
array1=np.array([[1,2,3],[4,5,6]])
array2=np.array([[4,5,6],[1,2,3]])
array3=np.concatenate((array2,array1),axis=0)
print(array3)
array3=np.concatenate((array2,array1),axis=1)
print(array3)