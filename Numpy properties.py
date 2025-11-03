#  if there are different type of values in a numpy function then it will change the other values in following order 1.String 2.complex 3.float 4. integer 5.boolean

import numpy as np

y = np.array([1, "you", True])

print(y)
