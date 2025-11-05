import ast 
input_list=ast.literal_eval(input())
m=int(input())
n=int(input())

import numpy as np
array_1 = np.array(input_list)
final_array = array_1[m:n+1]

print(final_array)

