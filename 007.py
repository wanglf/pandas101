# 7. How to get the items not common to both series A and series B?
# Q. get all items of ser1 and ser2 not common to both.

import numpy as np
import pandas as pd

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser_u = pd.Series(np.union1d(ser1, ser2)) # union
ser_i = pd.Series(np.intersect1d(ser1, ser2)) # intersect

result = ser_u[~ser_u.isin(ser_i)]
print(repr(result))