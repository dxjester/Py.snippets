# def scatter plot function (df, x_val, y_val, color):

  temp_df = df[[x_val, y_val]]
  temp_df = temp_df.groupby(x_val).sum().resent_index()
  
  title = x_val + ' and ' + y_val + ' Linear Timeries Plot'
  
  x_val = temp_df[x_val]
  y_val = temp_df[y_val]
  
  plot.scatter(x_val, y_val, color = color)
  plt.figure(figsize=(10,10))
  plt.title(title)
  plt.grid()
  plt.show()
