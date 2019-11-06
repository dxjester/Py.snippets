#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:15:01 2019

@author: patrickbenitez
"""

# CATEGORY: dataframe, pandas, column, row
def set_check_in_df(set_var, df, df_col_name):
    '''
    a function to return matching set values located within a given dataframe
    '''
    assert type(set_var) is set
    matches = df[df_col_name].apply(lambda x: x in set_var)
    return df[matches]



# CATEGORY: string, char, manipulation, slicing
def find_description(str_var, df, df_col_name):
    matches = df[df_col_name].str.contains(str_var)
    return df[matches]



# CATEGORY: dataframe, merge, column
def find_two_away(code, df):
    one_away = df[df['ORIGIN_AIRPORT_ID'] == code]
    two_away = one_away.merge(df, left_on = 'DEST_AIRPORT_ID', right_on = 'ORIGIN_AIRPORT_ID')
    return set(two_away['DEST_AIRPORT_ID_y'])



# CATEGORY: dataframe, pandas, convert
def calc_who_switched(Drugs):
    who_switched = Drugs.groupby(['ID'])['Med'].unique().to_frame(name='Unique Med')
    return who_switched



# CATEGORY: numpy, array, convert, datatype
# convert array data type
B = np.array([[False, True,  False],
              [False, False, True],
              [True,  True,  False]])

A = B.astype(int)
print(A)

# CATEGORY: scipy, coo_matrix, matrix, numpy
# initialize an integer boolean (1,0) array
def make_board(coords_df, n=50):
    ### BEGIN SOLUTION
    row = coords_df['x']
    col = coords_df['y']
    val = [1] * len(row)
    board = coo_matrix((val, (row, col)), shape=(n, n))
    board = board.toarray()
    return board



# CATEGORY: plot, seaborn, pair plot
# plots 5 x 5 pair plot of a given dataframe
import seaborn as sns
sns.pairplot(filtered_data[['revenue','budget','popularity', 'vote_average','vote_count']])



# CATEGORY: plot, seaborn, pair plot
# plots a scatterplot
import matplotlib.pyplot as plt
import numpy as np
import random 

x = [2*i for i in range(10)]
y = [i**2 for i in range(10)]
fig = plt.figure(figsize = (10,6))
ax = fig.add_subplot(111)
ax.scatter(x,y, color='red', linewidth=3)
ax.set(title='Scatterplot',  ylabel='i-squared', xlabel='2 * i')
plt.show()



# CATEGORY: time, date, datetime, calendar, for loop, iterate
from dateutil import rrule
from datetime import datetime, timedelta

now = datetime.now()
hundredDaysLater = now + timedelta(days=100)

for dt in rrule.rrule(rrule.MONTHLY, dtstart=now, until=hundredDaysLater):
    print(dt)



# CATEGORY: time, date, datetime, calendar, for loop, iterate    
# calcuate start and end times
import time

start = time.time()
print("hello")
end = time.time()

# CATEGORY: user input, user, prompt, integer
# prompt a user for an input
size = int(input("Enter a number: "))
size = float(input("Enter a number: "))

# CATEGORY: random, randomize, integer
# create a randomized list of integers
from numpy.random import seed
from numpy.random import randint
values = randint(0, 50, 100)
print (values)

# CATEGORY: lambda, function, boolean, apply, lambda function
# assign a boolean value in a new calculate column base on a given column's values
who_switched['Med A->B?'] = who_switched.apply(lambda x: 1 if len(x['Unique Med'])==2 else 0,axis=1)

# CATEGORY: Pearson, correlation, coefficient, numpy
def corr_coeff(col1,col2):
    import numpy as np
    return np.corrcoef(col1, col2)[0,1]

# CATEGORY: format, formatting
print('The dataset has {} rows.'.format(len(credit))) 

# CATEGORY: regex, split, pandas, column
# split a column value (i.e. '8.9 1/1/2020') into two separate columns using regex
df_copy['test_value'] = df['result_date_taken'].str.extract(r'(\d+\.?\d+)').astype(np.float64) 
df_copy['date_taken'] = df['result_date_taken'].str.extract(r'(\d+[-/]\d+[-/]\d+)') 