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

# CATEGORY: sort, sorting, pandas, dataframe, column, columns, 
# sort a dataframe by a list of columns
desired_cols = ['avg','team']
desired_cols.sort()

# CATEGORY: column, rename, dataframe, header
# rename dataframe columns
home_df.rename(columns = {'home_diff':'differential'}, inplace = False) 

# CATEGORY: numpy, apply, function, conditional, compare, comparison, where
# numpy's where function to assign values given a column value
copy_df['winner'] = np.where(copy_df.goal_diff > 0, copy_df.home_team, copy_df.away_team)

# CATEGORY: round, number, math
# round a quantifiable value
sorted_df = sorted_df.round(3)

# CATEGORY: regex, regular, regular expression, expression, filter, column, panda, dataframe
# utilize a regex function to remove columns containing a specific value
data = df[df.columns.drop(list(df.filter(regex='OTHER')))]
data_header = df_header[df_header.columns.drop(list(df.filter(regex='OTHER')))]
print ("\n".join(data.columns))

# CATEGORY: delete, column, panda, dataframe
# delete a column name in a pandas dataframe
del df14_work['Q6']
df3 = df3.drop(['venue_state'], axis=1)

# CATEGORY: mask, dataframe, panda
# filter a dataframe based on a mask
df = df[~df['onsale_dt'].isnull()]

# CATEGORY: impute, fillna, nan, NaN, null, dataframe
# impute missing nan / null values in a dataframe
df40.fillna(0, inplace = True)

# CATEGORY: pivot, panda, dataframe, transpose
# pivot a dataframe
df40_pivot = df40.pivot(index='userId', columns='movieId', values='rating')
df40_array = df40_pivot.values

# CATEGORY: type change, data, type, dtype
# change a column's data type
df40_reset['userId'] = df40_reset['userId'].astype(int)

# CATEGORTY: dictionary, comprehension
# dictionary comprehension
user_id_index = {c: i for i, c in enumerate(df40_reset['userId'])}

# CATEGORY: dictionary, append, 
# fill dictionary value with for loop
from collections import defaultdict
cosine_dict = defaultdict()
cosine_val = 0
for user_id,user_index in dict42.items():
    #print(str(user_id)+': '  + str(user_index))
    #print(matrix[user_index])
    vector_user = matrix[user_index]
    cosine_val = cosine(user22_vector, vector_user)
    cosine_dict[user_id] = cosine_val

