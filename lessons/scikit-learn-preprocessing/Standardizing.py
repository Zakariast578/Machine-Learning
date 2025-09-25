import numpy as np
from sklearn.preprocessing import scale

# Assignment link:
#https://g.co/gemini/share/d1e3c4d859b2

# Standardizing Data
# Use scikit-learn to standardize data.

#A. Standard data format#

#B. NumPy and scikit-learn#
# Create a sample NumPy array
data = np.array([[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0],
                 [7.0, 8.0, 9.0]])
print("Original NumPy array:\n{}".format(data))
# Standardizing each column of pizza_data
col_standardized = scale(data)
print('{}\n'.format(repr(col_standardized)))

# Column means (rounded to nearest thousandth)
col_means = col_standardized.mean(axis=0).round(decimals=3)
print('{}\n'.format(repr(col_means)))

# Column standard deviations
col_stds = col_standardized.std(axis=0)
print('{}\n'.format(repr(col_stds)))