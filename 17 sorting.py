import numpy as np

vector_unsorted=np.array([2,4,6,8,5,3,2,5,7,6,4,1,35,9])
print("sorted vector: ",np.sort(vector_unsorted))

array_unsorted=np.array([[3,1],[2,1],[3,2]])
print("array sorted(axis=0): ",np.sort(array_unsorted,axis=0))
print("array sorted(axis=1): ",np.sort(array_unsorted,axis=1))