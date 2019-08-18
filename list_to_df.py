import pandas as pd

simple_list=[['a','b']]
simple_list.append(['e','f'])

df=pd.DataFrame(simple_list,columns=['col1','col2'])


   col1 col2
0    a    b
1    e    f
