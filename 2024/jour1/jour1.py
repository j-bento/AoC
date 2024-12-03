import sys
import os
from collections import Counter

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

from helper import *

# Part 1
file = read_input(current, Choice.REAL)
lList, rList = [], []
for line in file:
    lElt, rElt = [int(elt) for elt in line.split()]
    lList.append(lElt)
    rList.append(rElt)
# both lists should have the same length
_sum = 0
for i in range(len(lList)):
    lMin = min(lList)
    rMin = min(rList)
    _sum += abs(rMin - lMin)
    lList.remove(lMin)
    rList.remove(rMin)
print(_sum)

# Part 2
file = read_input(current, Choice.REAL)
lList, rList = [], []
for line in file:
    lElt, rElt = [int(elt) for elt in line.split()]
    lList.append(lElt)
    rList.append(rElt)

_sum = 0
# count the occurrences with the help of the Counter class
counter = Counter(rList)
for elt in lList:
    _sum += elt * counter[elt]
print(_sum)