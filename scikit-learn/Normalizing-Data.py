import numpy as np
import pandas as pd
#Assignment link:
#https://g.co/gemini/share/d1e3c4d859b2

#Normalizing Data
#Use scikit-learn to normalize data.

#A. L2 normalization#
data = np.array([[4.0, 1.0, 2.0, 2.0],
                 [1.0, 3.0, 9.0, 3.0],
                 [5.0, 7.0, 5.0, 1.0]])
print('{}\n'.format(repr(data)))

from sklearn.preprocessing import Normalizer
normalizer = Normalizer()
transformed = normalizer.fit_transform(data)
print('{}\n'.format(repr(transformed)))