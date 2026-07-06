import numpy as np
array1=np.array([[1,2],[4,5]])
print(array1 + 5)
print(array1 *5)
print(array1 ** 2)  


array2=np.array([[10,20],[40,50]])

# Matrix addn
print("Matrix addition\n",array1+array2)

# Matrix Subtraction
print("Matrix subtraction\n",array1-array2)



print("Matrix Multiplication\n",array1*array2) # this does dot function


# Matrix Multiplication
# method 1
print("Matrix Multiplication\n",np.matmul(array1,array2)) #this does multiplication

# method 2
print("Matrix Multiplication\n",array1@array2)



# transpose of a matrix

# method 1
print("transpose of array1: \n",array1.T) 

# method 2
print("transpose of array1: \n",np.transpose(array1)) 



# how to find determinant

print("Determinant of Array2: ",np.linalg.det(array2))


# how to find inverse of a matrix
print("inverse of array1: \n",np.linalg.inv(array1))



# how to find inverse of a matrix
print("trace of array1: \n",np.linalg.trace(array1))
print("trace of array2: \n",np.linalg.trace(array2))



# how to find rank of a matrix
print("rank of array1 : \n",np.linalg.matrix_rank(array1))




# how to find eigen value and eigen vector of a matrix


print("eigen value of array2 : \n",np.linalg.eig(array2))