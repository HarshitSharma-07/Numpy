import numpy as np

# this is exactly like masking

numbers=np.array([21,43,23,65,97,34,75,23,86,45,86,48,97])

where_result=np.where(numbers>50)
print("where_result: ",where_result)
print("numbers greater than 50: ",numbers[where_result])


# another way to use where function

conditional_Array=np.where(numbers>50,numbers*4,numbers)
print(conditional_Array)
# take this as:
# if(numbers>5)
# {
#     numbers*4
# }
# else
# {
#     numbers
# }


# another example:
data=np.array([1,2,3,4,5,6,7,8,9,10])
where_result=np.where(data>5,True,False)
print(where_result)