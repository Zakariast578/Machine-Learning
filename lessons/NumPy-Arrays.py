#A. Arrays #
import numpy as np # type: ignore

arr = np.array([[0, 1, 2], [3, 4, 5]],
               dtype=np.float32)
print(repr(arr))

#B Coppying Arrays #
a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 5
print('Array a: {}'.format(repr(a)))
print(repr(c))

d = b.copy()
d[0] = 6
print('Array b: {}'.format(repr(b)))
print(repr(d))

#C. Casting # The code below shows an example of casting using the astype function. The dtype property returns the type of an array.
arr = np.array([0, 1, 2])
print(arr.dtype)
arr = arr.astype(np.float32)
print(arr.dtype)

#D. NaN #
arr = np.array([np.nan, 1, 2])
print(repr(arr))

arr = np.array([np.nan, 'abc'])
print(repr(arr))

# Will result in a ValueError: If we uncomment line 8 and run again.
#np.array([np.nan, 1, 2], dtype=np.int32)
np.array([np.nan, 1, 2], dtype=np.float32)

#E. Infinity #
arr = np.array([np.inf, 1, 2])
print(repr(arr))
arr = np.array([-np.inf, 1, 2])
print(repr(arr))
arr = np.array([np.inf, -np.inf, np.nan])
print(repr(arr))