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
# DESCRIPTION:round a quantifiable value
sorted_df = sorted_df.round(3)

# CATEGORY: regex, regular, regular expression, expression, filter, column, panda, dataframe
# DESCRIPTION: utilize a regex function to remove columns containing a specific value
data = df[df.columns.drop(list(df.filter(regex='OTHER')))]
data_header = df_header[df_header.columns.drop(list(df.filter(regex='OTHER')))]
print ("\n".join(data.columns))

# CATEGORY: delete, column, panda, dataframe
# DESCRIPTION: delete a column name in a pandas dataframe
del df14_work['Q6']
df3 = df3.drop(['venue_state'], axis=1)

# CATEGORY: mask, dataframe, panda
# DESCRIPTION: filter a dataframe based on a mask
df = df[~df['onsale_dt'].isnull()]

# CATEGORY: impute, fillna, nan, NaN, null, dataframe
# DESCRIPTION: impute missing nan / null values in a dataframe
df40.fillna(0, inplace = True)

# CATEGORY: pivot, panda, dataframe, transpose
# DESCRIPTION: pivot a dataframe
df40_pivot = df40.pivot(index='userId', columns='movieId', values='rating')
df40_array = df40_pivot.values

# CATEGORY: type change, data, type, dtype
# DESCRIPTION: change a column's data type
df40_reset['userId'] = df40_reset['userId'].astype(int)

# CATEGORTY: dictionary, comprehension
# DESCRIPTION: dictionary comprehension
user_id_index = {c: i for i, c in enumerate(df40_reset['userId'])}

# CATEGORY: dictionary, append, 
# DESCRIPTION: fill dictionary value with for loop
from collections import defaultdict
cosine_dict = defaultdict()
cosine_val = 0
for user_id,user_index in dict42.items():
    #print(str(user_id)+': '  + str(user_index))
    #print(matrix[user_index])
    vector_user = matrix[user_index]
    cosine_val = cosine(user22_vector, vector_user)
    cosine_dict[user_id] = cosine_val

# CATEGORY: panda, pandas, dataframe
# DESCRIPTION: return cell value (with row and column) in dataframe
sub_df.iloc[0]['A']


# CATEGORY: plot, scatter, panda, dataframe, scatterplot
# DESCRIPTION: plot a simple scatter plot
from matplotlib.pyplot import scatter, xlabel, ylabel, title,plot
x = [0,1,2,3,4,5,6,7,8,9,10]
y = [i**2 for i in x]

scatter(x,y)
xlabel("X Value")
ylabel("Y Value")
title("Scatterplot Plot")


# CATEGORY: time, calculation, timeit
# DESCRIPTION: calculate the time for an operation to complete
n = 100000
L = range(n)
%timeit [i**2 for i in L]

# CATEGORY: for, loop, range
# DESCRIPTION: use a left and right parameter for range function
for k in range(2, int(sqrt(n))+1):
    is_prime[2*k::k] = False
    
<<<<<<< HEAD
    
    emails = []
    for items in data:
        emails.append(items['email']['working'])
    emails.sort(reverse = True)
    return emails

# CATEGORY: for, loop, range, list, sort
# DESCRIPTION: a function to append values to an empty list and sort
def sort_list():
    emails = [] 
    for items in data:
        emails.append(items)
    emails.sort(reverse = True)
    return emails

# CATEGORY: split, nested, JSON, column dataframe
# DESCRIPTION: split nested JSON data in a column to separate columns
df = pd.DataFrame({'a':[1,2,3], 'b':[{'c':1}, {'d':3}, {'c':5, 'd':6}]})
df
df['b'].apply(pd.Series)
=======

# CATEGORY: pandas, panda, groupby , count , column, 
# DESCRIPTION: retrieve specific columns, aggregate and group by to get counts
flights_cols_subset = flights[['FL_DATE', 'ORIGIN_AIRPORT_ID', 'DEST_AIRPORT_ID']]
segment_groups = flights_cols_subset.groupby(['ORIGIN_AIRPORT_ID', 'DEST_AIRPORT_ID'], as_index=False)
segments = segment_groups.count()
segments.rename(columns={'FL_DATE': 'FL_COUNT'}, inplace=True)
segments.head()


# CATEGORY: pandas, panda, rename, column,
# DESCRIPTION: rename columns in pandas dataframe
dests.rename(columns={'FL_COUNT': 'DEST_COUNT'}, inplace=True)



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
\b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"r"ain\b"	
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

str = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", str)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
  

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start()) 


# split at each whitespace character
str = "The rain in Spain"
x = re.split("\s", str)
print(x)

# split only at the first occurence
str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)

# use the sub function to replace whitespace character w/ '9'
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x)

# CATEGORY: json, dictionary, convert, conversion
# DESCRIPTION: convert a Python dictionary to a JSON file
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
print(y)


# CATEGORY: sql, query, pandas, dataframe, database, connection
# DESCRIPTION: pass a SQL query through a connection and read in as a pandas dataframe
Persons = pd.read_sql_query('SELECT * FROM Persons', conn)



# CATEGORY: sql, query, pandas, dataframe, database, connection
# DESCRIPTION: read in multiple files based on conditional formatting
master_df = []

for yy in range(11,15):
    filename = "statoutflow{}{}".format(yy,yy+1)
    df = pd.read_csv(fn(filename),encoding='latin-1')
    df['year'] = 2000 +yy
    
# CATEGORY: apply, function, filter, mask
# DESCRIPTION: create a mask, apply to a df and pull only select columns
def ends_in (pattern, s):
    import re
    return re.match ("^.*{}$".format (pattern), s) is not None

def ends_in_total_migration (s):
    return ends_in ('Total Migration[ -]US and Foreign', s)

def ends_in_non_migrants (s):
    return ends_in ('Non-migrants', s)


migrants = StateOutFlows['y2_state_name'].apply (ends_in_total_migration)
migrants.head(5)


Migrated = StateOutFlows[migrants][['y2_state', 'year', 'n1']] \
           .rename (columns={'y2_state': 'st', 'n1': 'migrated'})
Migrated
    alldf.append(df)
    
# CATEGORY: list, extend, list of lists, function
# DESCRIPTION: Invoke the extend function to flatten two lists as a single list
my_list = ['geeks', 'for'] 
another_list = [6, 0, 4, 1] 
my_list.extend(another_list) 
print(my_list) 


# CATEGORY: pandas, panda, dataframe 
# DESCRIPTION: consolidate all dataframe columns or column as a single array
# importing pandas as pd 
import pandas as pd 
  
# Creating the DataFrame 
df = pd.DataFrame({'Weight':[45, 88, 56, 15, 71], 
                   'Name':['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'], 
                   'Age':[14, 25, 55, 8, 21]}) 
>>>>>>> baab3d9c935333e9e0b9e5f0f5d139997e1566a7
