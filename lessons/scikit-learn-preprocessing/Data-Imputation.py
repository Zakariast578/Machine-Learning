import pandas as pd
import numpy as np

#Assignment link:
#https://g.co/gemini/share/d1e3c4d859b2

#Data Imputation
#Use scikit-learn to impute missing data.

# Data imputation models
data = np.array([[1, 2, np.nan, 3],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])
print('{}\n'.format(repr(data)))
# predefined data
print('{}\n'.format(repr(data)))

from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer()
transformed = imp_mean.fit_transform(data)
print('{}\n'.format(repr(transformed)))

# predefined data
print('{}\n'.format(repr(data)))

from sklearn.impute import SimpleImputer
imp_median = SimpleImputer(strategy='median')
transformed = imp_median.fit_transform(data)
print('{}\n'.format(repr(transformed)))

imp_frequent = SimpleImputer(strategy='most_frequent')
transformed = imp_frequent.fit_transform(data)
print('{}\n'.format(repr(transformed)))

# predefined data
print('{}\n'.format(repr(data)))

from sklearn.impute import SimpleImputer
imp_constant = SimpleImputer(strategy='constant',
                             fill_value=-1)
transformed = imp_constant.fit_transform(data)
print('{}\n'.format(repr(transformed)))

#B. Other imputation methods#
