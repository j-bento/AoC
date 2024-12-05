import sys
import os
import functools

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

from helper import *

ordering_dict = {}
# custom comparator to compare the elements of each list
def compare(x, y):
    res = 0
    if y in ordering_dict:
        res = 1 if x in ordering_dict[y] else -1
    if x in ordering_dict:
        res = -1 if y in ordering_dict[x] else 1
    return res  

# Part 1
file = read_input(current, Choice.REAL)
ordering_lines, lines = ''.join(file.readlines()).split('\n\n')

# dictionary that stores the list of all the elements after an element
for line in ordering_lines.split('\n'):
    elt, elt_after = [int(e) for e in line.split('|')]
    if elt in ordering_dict: # append to existing list
        ordering_dict[elt].append(elt_after)
    else: # create a new list
        ordering_dict[elt] = [elt_after]

res = 0
for line in lines.split('\n'):
    elts = [int(e) for e in line.split(',')]
    newElts = sorted(elts, key=functools.cmp_to_key(compare))
    # add the middle element if the list is already correct
    if elts == newElts:
        res += elts[len(elts)//2]
    
print(res)

# Part 2
res = 0
for line in lines.split('\n'):
    elts = [int(e) for e in line.split(',')]
    newElts = sorted(elts, key=functools.cmp_to_key(compare))
    # add the middle element of the corrected list
    if elts != newElts:
        res += newElts[len(newElts)//2]
        
print(res)