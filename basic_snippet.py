#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:15:01 2019

@author: patrickbenitez
"""

# a function to return matching set values in a dataframe
def set_check_in_df(set_var, df, df_col_name):
    '''
    a function to return matching set values located within a given dataframe
    '''
    assert type(set_var) is set
    matches = df[df_col_name].apply(lambda x: x in set_var)
    return df[matches]

# a string function to check if cells contain a specific string
def find_description(str_var, df, df_col_name):
    matches = df[df_col_name].str.contains(str_var)
    return df[matches]

# CATEGORY: dataframe, merge, column
def find_two_away(code, df):
    one_away = df[df['ORIGIN_AIRPORT_ID'] == code]
    two_away = one_away.merge(df, left_on = 'DEST_AIRPORT_ID', right_on = 'ORIGIN_AIRPORT_ID')
    return set(two_away['DEST_AIRPORT_ID_y'])
    