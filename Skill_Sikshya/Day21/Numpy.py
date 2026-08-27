# Indexing and Slicing Arrays in Numpy

import numpy as np

#1D Array

a = np.array([1,2,3,4,5])
print(a[3])
print(a[2::1])
print(a[::-1])

# 2D Array

arr = np.random.randint(0,10, size = (5,4))
print(arr)

print(arr[2, -1])  # gives element of row at index 2 and its last element

print(arr[-1, -1])  # gives the last element of the matrix

print(arr[1:4])

print(arr[1:4, 2:])


print(arr[:, -1:])   # gives the last column


print(arr[2:4, 1:3])


#3D Array

np.random.seed(99)

arr = np.random.randint(0,10, size = (3,4,3))

print(arr)

# Indexing
print("\n", arr[1,-1,0])

#Slicing
print(arr[::, 1, -2:])


dataset = np.random.randint(0,255, size = (16,3,720,720)) / 255
print(dataset)


import matplotlib.pyplot as plt
print(dataset.shape)
print(dataset[-1].shape)
print(dataset[-1].size)
plt.imshow(dataset[-1].reshape(720, 720, 3))
plt.axis("off")
plt.show()




