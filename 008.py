# 8. How to get the minimum, 25th perentile, median, 75th, and max of a numeric series?
# Q. Compute the minimum, 25th percentile, median, 75th, and maximum of ser.

import numpy as np
import pandas as pd

state = np.random.RandomState(100)
ser = pd.Series(np.random.normal(10, 5, 25))

# Solution
result = np.percentile(ser, q=[0, 25, 50, 75, 100])
print(repr(result))

