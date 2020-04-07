import math
import os
import random
import re
import sys

matrix = [[j+1 for j in range(5)] for i in range(5)]
print(matrix)

new_matrix = []
for itr in matrix:
    for itr1 in itr:
        new_matrix.append(itr1)
print(new_matrix)

new_matrix2 = [val for itr in matrix for val in itr ]
print(new_matrix2)
print('first commit')

