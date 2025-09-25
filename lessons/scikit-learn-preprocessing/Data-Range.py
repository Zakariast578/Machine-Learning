import pandas as pd
import numpy as np

# Assignment link:
#https://g.co/gemini/share/d1e3c4d859b2

#Data Range
#Use scikit-learn to scale data to a specified range.

#A. Range scaling#
#B. Range compression in scikit-learn#
data = np.array([[1.0, -1.0, 2.0],
                 [2.0, 0.0, 0.0],
                 [0.0, 1.0, -1.0]])
# predefined data
print('{}\n'.format(repr(data)))

from sklearn.preprocessing import MinMaxScaler
default_scaler = MinMaxScaler() # the default range is [0,1]
transformed = default_scaler.fit_transform(data)
print('{}\n'.format(repr(transformed)))

custom_scaler = MinMaxScaler(feature_range=(-2, 3))
transformed = custom_scaler.fit_transform(data)
print('{}\n'.format(repr(transformed)))

new_data = np.array([[2.0, -2.0, 3.0],
                     [3.0, -1.0, 4.0]])
# predefined new_data
print('{}\n'.format(repr(new_data)))

from sklearn.preprocessing import MinMaxScaler
default_scaler = MinMaxScaler() # the default range is [0,1]
transformed = default_scaler.fit_transform(new_data)
print('{}\n'.format(repr(transformed)))

default_scaler = MinMaxScaler()  # new instance
default_scaler.fit(data)  # different data value fit
transformed = default_scaler.transform(new_data)
print('{}\n'.format(repr(transformed)))