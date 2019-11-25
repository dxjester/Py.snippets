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


# CATEGORY: regular, expressions, regex, re
# DESCRIPTION: Summary of commonly used regex terminology
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")

''' 
Character	Description	Example	Try it
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"	
()	Capture and group	 
'''

'''
[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
'''

'''
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

'''

# CATEGORY: regular, expressions, regex, re
# DESCRIPTION: find all function
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)