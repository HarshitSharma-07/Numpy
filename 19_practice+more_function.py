import numpy as np
import matplotlib.pyplot as plt

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print("==== Food Delivery Sales Data Analysis ====")
print("Data Shape: ",sales_data.shape)
print("First 3 Rows: ",sales_data[:3])

print(np.sum(sales_data,axis=0))
yearly_data=np.sum(sales_data[:,1:],axis=0)
print(yearly_data)

# min sales
min_sales=np.min(sales_data[:,1:],axis=1)
print(min_sales)


# max sales
max_sales=np.max(sales_data[:,1:],axis=0)
print(max_sales)



# average sales
avg_sales=np.average(sales_data[:,1:],axis=1)
print(avg_sales)


# cumulative sales
cum_sales=np.cumsum(sales_data[:,1:],axis=1)
print(cum_sales)


# matplotlib
plt.figure(figsize=(10,10))
plt.plot(np.mean(cum_sales,axis=0))
plt.title("average cumulative sales across all restaurants")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()




vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

print("Vector addition: ",vector1+vector2)

print("\n Multiplication vector", vector1*vector2)

print("\nDot Product", np.dot(vector1,vector2))

angle=np.arccos(np.dot(vector1,vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2)))
print(angle)



restaurant_types=np.array(["biryani","chinese","pizza","burger","cafe"])
vectorized_upper=np.vectorize(str.upper)
print("vectorized upper",vectorized_upper(restaurant_types))



array1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
array2=np.random.rand(3,3)
array3=np.zeros((4,4))

np.save('array1.npy',array1)
np.save('array2.npy',array2)
np.save('array3.npy',array3)


loaded_Array=np.load('array1.npy')
loaded_Array=np.load('array2.npy')
loaded_Array=np.load('array3.npy')



try:
    logo = np.load(r"C:\programming\python\numpy\numpy-logo.npy")
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.imshow(logo)
    plt.title("numpy logo")
    plt.grid(False)

    reverse_logo=1-logo
    plt.subplot(1,2,2)
    plt.imshow(reverse_logo)
    plt.title("numpy logo")
    plt.grid(False)

    plt.show()

except FileNotFoundError:
    print("numpy-logo file not found")