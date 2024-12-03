import sys
import os

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

from helper import *

# Part 1
file = read_input(current, Choice.REAL)
_sum = 0
for line in file:
    lst = [int(elt) for elt in line.split()]
    # evil boolean comprehension list 
    if all([lst[i] < lst[i + 1] and ( 1 <= abs(lst[i + 1] - lst[i]) <= 3) for i in range(len(lst) - 1)]) \
    or all([lst[i] > lst[i + 1] and ( 1 <= abs(lst[i + 1] - lst[i]) <= 3) for i in range(len(lst) - 1)]):
        _sum += 1
print(_sum)

# Part 2
file = read_input(current, Choice.REAL)
_sum = 0
for line in file:
    lst = [int(elt) for elt in line.split()]
    # evil boolean comprehension list + super evil bruteforce : try every list arrangement possible
    for i in range(len(lst)): 
        tmpLst = list(lst)
        tmpLst.pop(i)
        # we need only one arrangement that works
        if all([tmpLst[i] < tmpLst[i + 1] and ( 1 <= abs(tmpLst[i + 1] - tmpLst[i]) <= 3) for i in range(len(tmpLst) - 1)]) \
        or all([tmpLst[i] > tmpLst[i + 1] and ( 1 <= abs(tmpLst[i + 1] - tmpLst[i]) <= 3) for i in range(len(tmpLst) - 1)]):
            _sum += 1
            break
print(_sum)