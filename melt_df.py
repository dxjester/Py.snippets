'# create a dataframe utilizing the melt function

columns = ['category_col1', 'category_col2', 'category_col3', 'category_col4', 'category_col5']
number_col = ["FY11", "FY12","FY13","FY14","FY15"]

melt_df = master_df.melt(id_vars=column, value_vars=spend_column, var_name = 'Fiscal Year', value_name = 'Value')
