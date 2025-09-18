import pandas as pd
import numpy as np

#Note Link:
#https://g.co/gemini/share/1c644411363a

#Series Creation
import pandas as pd
import numpy as np

# Creating an empty series, will result in DeprecationWarning
#series = pd.Series()

# Passing dtype as a parameter to Series for an empty series to avoid DeprecationWarning
# Creating an empty series
series = pd.Series(dtype='float64')
# Newline to separate series print statements
print('{}\n'.format(series))

series = pd.Series(5)
print('{}\n'.format(series))

series = pd.Series([1, 2, 3])
print('{}\n'.format(series))

series = pd.Series([1, 2.2]) # upcasting
print('{}\n'.format(series))

arr = np.array([1, 2])
series = pd.Series(arr, dtype=np.float32)
print('{}\n'.format(series))

series = pd.Series([[1, 2], [3, 4]])
print('{}\n'.format(series))

#B. Index#
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print('{}\n'.format(series))

series = pd.Series([1, 2, 3], index=['a', 8, 0.3])
print('{}\n'.format(series))

#C. Dictionary input#
series = pd.Series({'a':1, 'b':2, 'c':3})
print('{}\n'.format(series))

series = pd.Series({'b':2, 'a':1, 'c':3})
print('{}\n'.format(series))

