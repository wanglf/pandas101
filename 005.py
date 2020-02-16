# How to assign name to the series' index?
# Q. Give a name to the series ser calling it 'alphabets'.

import numpy as np
import pandas as pd

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))

# Solution
ser.name = 'alphabets'
print(repr(ser.head()))