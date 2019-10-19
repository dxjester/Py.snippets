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

# Create a multi-dimensional array 
m_array = np.array([
        [0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]
        ])

print(m_array)

