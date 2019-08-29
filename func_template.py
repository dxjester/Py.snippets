
def fiscal_year_conversion(filename):
  '''
    The purpose of this function is to standardize the fiscal year columns
  '''
  
  if "FY13" in filename:
    return 2013
  elif "FY14 in filename: 
    return 2014
  elif "FY14 in filename: 
    return 2015
  else:
    return null
    
# application of function
master_df['fiscal_year'] = master_df['fiscal_year'].apply(fiscal_year_conversion)
