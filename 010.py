# 10. How to keep only top 2 most frequent values as it is and replace everything else as 'Other'?
# Q. From ser, keep the top 2 most frequent items as it is and replace everything else as 'Other'.

import numpy as np
import pandas as pd

np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

# Solution
print("Top 2 Freq: ", ser.value_counts())
ser[~ser.isin(ser.value_counts().index[:2])]='Other'
print(repr(ser))