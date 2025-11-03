#  if there are different type of values in a numpy function then it will change the other values in following order 1.String 2.complex 3.float 4. integer 5.boolean

import numpy as np

y = np.array([1, "you", True])

print(y)


#Arthmatic operations in list vs numpy

list1 = [1,3,4,6]
list2 = [3,4,3]

print (list1 + list2)

np_list1 = np.array([1,3,4,6])
np_list2 = np.array([3,4,3,7]) # if the length of both the numpy arrays are not same it will give error

print (np_list1 + np_list2)
