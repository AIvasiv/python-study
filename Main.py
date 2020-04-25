import math
import os
import random
import re
import sys

from pip._vendor.distlib.compat import raw_input

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

def hackerrank_NestedList():
    """Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
        Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line."""

def hackerrank_Lists():
    N = input()
    l = []
    for _ in range(N):
        s = raw_input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("l." + cmd)
        else:
            print
            l

