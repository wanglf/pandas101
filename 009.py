# 9. How to get frequency counts of unique items of a series?
# Q. Calculate the frequency counts of each unique value ser.

import numpy as np
import pandas as pd

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

# Solution
print(repr(ser.value_counts()))