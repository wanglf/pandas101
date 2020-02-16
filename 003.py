# 3. How to convert the index of a series into a column of a dataframe?
# Convert the series ser into a dataframe with its index as another column on the dataframe.

import numpy as np
import pandas as pd

mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

ser = pd.Series(mydict)

# Solution
df = ser.to_frame().reset_index()
print(df.head())