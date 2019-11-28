#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:11:14 2019

@author: patrickbenitez
"""

import numpy as np

a = np.array([1,2,3,4])
print(a)

n = 1000000

# CATEGORY: numpy, random, random int, create
# DESCRIPTION: Create a random numpy array
import numpy as np
ray_1 = np.random.randint(10, size =(3,3,3))
print(ray_1)

ray_1.shape # return shape of array
ray_1.dtype.name # returns data type of array

ray_2 = np.random.randint(5, size=(3,3,3))
print(ray_2)

ray_add = ray_1 + ray_2
print(ray_add)

ray_minus = ray_1 - ray_2
print(ray_minus)

ray_multiply = ray_1 * ray_2
print(ray_multiply)

ray_exp = ray_1 ** ray_2
print(ray_exp)

ray_1
ray_1.T




# Exercise 10.0 -------------------------------------------- #

# Test time for creating i^2 calculation via list call
L = range(n)
print ("Running equation n^2 loop via list command for timing purposes ... \n")
%timeit [i**2 for i in L]

# Test time for creating i^2 calculation via numpy array call
np.arange(10) # Moral equivalent to `range`
A = np.arange(n)
%timeit A**2

# Create a multi-dimensional array - example 1
m_array = np.array([
        [0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]
        ])

print(m_array)

print(m_array.ndim) # Print number of dimensions of array - '2'
print(m_array.shape) # Print shape of array - '3 (y axis for array),4 (x axis for array' 
print(len (m_array)) # Print length of array - '3' (for 3 x lists)

# initialize structured matrices
print (np.zeros((3,4)))
print (np.eye(3))
print(np.diag([1, 2, 3]))

A = np.empty((3, 4)) # An "empty" 3 x 4 matrix
print(A)

# 10.1: Matrix slicing 
print (m_array)
slice_list = m_array[0,2,:]
print(slice_list)

# 10.2: Slicing an array
Z= np.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]])

# Construct `Z_green`, `Z_red`, `Z_orange`, and `Z_cyan`:

Z_orange = Z[0, 3:5]
Z_red = Z[:, 2]
Z_green = Z[2::2, :2]  # starting at row 2, increment every 2 x-axis rows, 
Z_cyan = Z[4:, 4:]

print(Z_green)

# Indirect addressing
np.random.seed(3)
x =np.random.randint(0,20,15)
print(x)

# pull out random subsets
indexes = np.array([3,7,8,12])
print(x[indexes])

# create a boolean mask
mask_mult_3 = (x >0) & (x % 3 == 0)
print(mask_mult_3)

# CATEGORY: column, major, column major
# DESCRIPTION: map out index values from a m x n column major matrix to a linear matrix
def linearize_colmajor(i, j, m, n): # calculate `u`
    """
    Returns the linear index for the `(i, j)` entry of
    an `m`-by-`n` matrix stored in column-major order.
    """
    return i + j*m

n = 5000
A_colmaj = np.ones((n, n), order='F') # column-major (Fortran convention)
A_rowmaj = np.ones((n, n), order='C') # row-major (C/C++ convention)


# CATEGORY: row, major, row major
# DESCRIPTION: map out index values from a m x n row major matrix to a linear matrix
def linearize_rowmajor(i, j, m, n): # calculate `v`
    """
    Returns the linear index for the `(i, j)` entry of
    an `m`-by-`n` matrix stored in row-major order.
    """
    return i*n + j

n = 5000
A_colmaj = np.ones((n, n), order='F') # column-major (Fortran convention)
A_rowmaj = np.ones((n, n), order='C') # row-major (C/C++ convention)


# CATEGORY: matrix, matrices, calculation
# DESCRIPTION: add two matrices
import numpy as np
a = np.array([[2,4], [5,-6]])
b = np.array([[9,-3], [3,6]])

print("'a' array:\n ", a)
print("'b' array:\n ", b)

c_add = a+ b
print (c_add)

c_subtract = a - b
print (c_subtract)

c_multiply = a * b
print(c_multiply)

c_divide = a / b
print(c_divide)


# CATEGORY: matrix, dot, matrices, multiplication
# DESCRIPTION: utilize the dot function to multiply two matrices
import numpy.matlib 
import numpy as np 

a = np.array([[1,2], [3,4]])
b = np.array([[11,12], [13,14]])
print(np.dot(a,b))
# [[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]


# CATEGORY: pandas, panda, dataframe, column, names, header
# DESCRIPTION: create an empty dataframe with only column  names
import pandas as pd
df = pd.DataFrame(columns=['A','B','C','D','E','F','G'])



# CATEGORY: numpy, indices, find zero, zero, 
# DESCRIPTION: Find the indices of array elements that are non-zero, grouped by element.
import numpy as np
x = np.arange(6).reshape(2,3)
x
np.argwhere(x>1)

# CATEGORY: numpy, indices, linspace, meshgrid
# DESCRIPTION: Apply linspace and meshgrid functions for two given matrices
from numpy import linspace, meshgrid
x0 = linspace(-2,2,11)
x1 = linspace(-2,2,11)

X0, X1 = meshgrid(x0, x1)

# CATEGORY: numpy, colvec, transpose, vector, transform
# DESCRIPTION: Convert a vector from a row format to a column format
import numpy as np
z_array = np.array([1,2,3,4,5])
print(z_array)

z_colvec = np.reshape(z_array, (len(z_array), 1))
print(z_colvec)


# 