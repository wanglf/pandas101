# 4. How to combine many series to form a dataframe?
# Q. Combine ser1 and ser2 to form a dataframe.

import numpy as np
import pandas as pd

ser1 = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.DataFrame({'col1': ser1, 'col2': ser2})
print(df.head(10))