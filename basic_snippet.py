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