import numpy as np
from sklearn.preprocessing import RobustScaler

# Assignment link:
#https://g.co/gemini/share/d1e3c4d859b2

#A. Data outliers#
df = np.array([[1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 9.0],
                [1000.0, 2000.0, -3000.0]])
print('{}\n'.format(repr(df)))

def iqr_range(data):
    """Compute the interquartile range of a dataset."""
    q75, q25 = np.percentile(data, [75 ,25], axis=0)
    return q75 - q25
print('{}\n'.format(repr(iqr_range(df))))

#B. Robust scaling with scikit-learn#
robust_scaler = RobustScaler()
transformed = robust_scaler.fit_transform(df)
print('{}\n'.format(repr(transformed)))