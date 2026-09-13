# Assignment: Introduction to Linear Algebra and NumPy

# Objective:
# This assignment will help you build a solid understanding of basic Linear Algebra concepts using Python and the NumPy library.
# You'll learn to create and manipulate arrays, perform mathematical operations, and explore properties and methods of arrays.

# Working with NumPy
# NumPy is a powerful Python library for numerical computations, which allows easy manipulation of arrays and matrices.

# Task 1:

# Import the numpy library and check its version.

#Solution

import numpy as np
print(np.__version__)

# Creating a NumPy Array:
# NumPy arrays are a powerful way to store and process large datasets. In this section, you will learn to create arrays.

# Task 2:

# Create a 1D NumPy array from a Python list of numbers: [1, 2, 3, 4, 5].
# Create a 2D NumPy array of shape (3x3) using the numbers from 1 to 9.
# Generate an array of 10 evenly spaced values between 0 and 5.

# Solution

arr_1d = np.array([1, 2, 3, 4, 5])
print("1D array:", arr_1d)

arr_2d = np.array(range(1, 10)).reshape(3, 3)
print("2D array:\n", arr_2d)

arr_lin = np.linspace(0, 5, 10)
print("Evenly spaced array:", arr_lin)

# Indexing and Slicing Arrays:
# Indexing and slicing allow you to access and modify specific elements of an array.

# Task 3:

# Access the element in the second row, third column of the 2D array you created above.
# Slice the first two rows and the first two columns from the same array.
# Modify the value in the last row and first column to 100.

# Solution

element = arr_2d[1, 2]
print("Element at row 2, col 3:", element)

sliced = arr_2d[:2, :2]
print("Sliced (first 2 rows, first 2 cols):\n", sliced)

arr_2d[-1, 0] = 100
print("Modified array:\n", arr_2d)
# Properties and Methods of NumPy Arrays
# NumPy arrays have several useful properties and methods.

# Task 4:

# Find the shape, size, and data type of the 2D array.
# Change the 1D array into a 2D array of shape (5,1).
# Flatten a multi-dimensional array back into a 1D array.

# Solution

print("Shape:", arr_2d.shape)
print("Size:", arr_2d.size)
print("Dtype:", arr_2d.dtype)

reshaped = arr_1d.reshape(5, 1)
print("Reshaped 1D array to (5,1):\n", reshaped)

flattened = reshaped.flatten()
print("Flattened back to 1D:", flattened)

# Operations on NumPy Arrays
# Perform operations such as addition, subtraction, multiplication, and matrix multiplication on arrays.

# Task 5:

# Add 5 to every element in the 1D array.
# Multiply the 2D array by 3.
# Perform matrix multiplication between the following two arrays:

# Solution

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

added = arr_1d + 5
print("1D array + 5:", added)

multiplied = arr_2d * 3
print("2D array * 3:\n", multiplied)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
matmul = A @ B
print("Matrix multiplication A x B:\n", matmul)

# Understanding Broadcasting
# Broadcasting allows NumPy to work with arrays of different shapes during arithmetic operations.

# Task 6:

# Create a 3x3 matrix of ones and a 1D array of length 3.
# Add the 1D array to each row of the matrix using broadcasting.

# Solution  ----> help from gpt

matrix_ones = np.ones((3, 3))
vector = np.array([1, 2, 3])
broadcast_result = matrix_ones + vector
print("Matrix of ones:\n", matrix_ones)
print("1D vector:", vector)
print("Broadcasted addition result:\n", broadcast_result)