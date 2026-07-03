import numpy as np
#vstack for stacking vertically-row wise
#hstack for stacking horizontally-column wise
#creates a new stack

arr=np.array([1,2,3])
arr2=np.array([4,5,6])

print(np.hstack((arr,arr2)))
print(np.vstack((arr,arr2)))