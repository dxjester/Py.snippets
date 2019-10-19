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

L = range(n)
print ("Running equation n^2 loop via list command for timing purposes ... \n")
%timeit [i**2 for i in L]
