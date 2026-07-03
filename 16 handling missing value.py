import numpy as np
# 1. isnan 

# array=np.array([1,2,np.nan,4,5,np.nan,7,8])
# print(np.isnan(array))


# not possible
# print(np.nan==np.nan)



# 2. nan to num
# default value is zero(0)

# print(np.nan_to_num(array,nan=10000))
# print(array)




# 3. infinities
array=np.array([1,2,np.inf,4,5,-np.inf,7,8])
print(array)
cleaned_array=np.nan_to_num(array,posinf=10000,neginf=-10000)
print(cleaned_array)