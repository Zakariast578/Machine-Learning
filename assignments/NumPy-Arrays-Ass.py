import numpy as np # type: ignore

#Time to Code! #
### first array we'll create comes straight from a list of integers and np.nan. The list contains np.nan as the first element, and the integers from 2 to 5, inclusive, as the next four elements.Set arr equal to np.array applied to the specified list.###

list = [np.nan,2,3,4,5]
arr = np.array(list)
print(repr(arr))

#Set arr2 equal to arr.copy(), then set the first element of arr2 equal to 10.
arr2 = arr.copy()
arr2[0] = 10
print(repr(arr2))

#"""
#Set float_arr equal to np.array applied to a list with elements 1, 5.4, and 3, in that order.

#Set float_arr2 equal to arr2.astype, with argument np.float32.
#"""

float_arr = np.array([1, 5.4, 3])
float_arr2 = arr2.astype(np.float32)
print(repr(float_arr))
print(repr(float_arr2))

#Set matrix equal to np.array with a list of lists (representing the specified 2-D matrix) as the first argument, and np.float32 as the dtype keyword argument.
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.float32)
print(repr(matrix))