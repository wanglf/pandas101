# 2. How to create a series from a list, numpy array and dict?
# Q. Create a pandas series from each of the items below: a list, numpy and a dictionary

import numpy as np
import pandas as pd

mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)

print(repr(ser1))
print(repr(ser2))
print(repr(ser3))