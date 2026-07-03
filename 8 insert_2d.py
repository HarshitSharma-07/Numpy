# axis is imp 
import numpy as np
array=np.array([[1,2,3],[4,5,6],[7,8,9]])
new_array=np.insert(array,3,[1],axis=0)
print(new_array)
new_array=np.insert(array,3,[1],axis=1)
print(new_array)
new_array=np.insert(array,3,[1],axis=None)
print(new_array)