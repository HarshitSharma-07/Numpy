import numpy as np

# type 1

arr=np.array([20,40,60,80,100,120])
new_arr=arr-(arr*20/100)
print(new_arr)



# type 2

new_Arr_2=arr+100

print(new_Arr_2)


# type 3
# 2 array of different dimensions cannot be added, we need to reshape it first and then add it


arr2=np.array([[1,2,3],[4,5,6]])
# arr3=arr+arr2
# print(arr3)



# what we can do here is...
# arr3=arr+arr2.flatten()
# print(arr3)


# or

# arr3=arr2+arr.reshape(2,3)
# print(arr3)
