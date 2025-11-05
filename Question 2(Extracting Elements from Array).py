import ast 
input_list = ast.literal_eval(input())
m = int(input())
n = int(input())

import numpy as np
array_1 = np.array(input_list)

# filter values strictly between m and n
final_array = array_1[(array_1 > m) & (array_1 < n)]

print(final_array)
