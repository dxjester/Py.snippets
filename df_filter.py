# filter master dataframe with conditional statements
cond1 = master_df['company'] == 'Nike'
cond2 = master_df['shoe'] == 'Jordan'

# create new dataframe with filtered data
new_df = master_df[cond1 & cond2]
new_df.head(10)
