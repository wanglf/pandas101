# 6. How to get the items of series A not present in series B?
# Q. From ser1 remove items present in ser2.

import numpy as np
import pandas as pd

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

result = ser1[~ser1.isin(ser2)]
print(repr(result))