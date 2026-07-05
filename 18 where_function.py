import numpy as np

# this is exactly like masking

numbers=np.array([21,43,23,65,97,34,75,23,86,45,86,48,97])

where_result=np.where(numbers>50)
print("where_result: ",where_result)
print("numbers greater than 50: ",numbers[where_result])