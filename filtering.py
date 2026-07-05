import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11])
print(arr[arr<5])

even_number=arr[arr%2==0]
print(even_number)


# Filter with mask
# now what is mask???
# masks are expressions used for evaluation

# example:

mask=arr>5  #it stores nothing more than this expression, not any value or nothing, just this expression
print("numbers greater than 5: ",arr[mask])