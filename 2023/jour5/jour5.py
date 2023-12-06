import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from helper import *

# Part 1
# works with small examples, but consumes too much memory

# def map_object_to_another(lines, index):
#     mapping = {}
#     while lines[index] != '' and index < len(lines) - 1:
#         dest, source, _range = lines[index].split()
#         for j in range(int(_range)):
#             mapping[int(source) + j] = int(dest) + j
#         index += 1
#     return mapping, index + 2

# lines = read_input(current,Choice.TEST).split('\n')
# mappings = []
# seeds = [int(x) for x in lines[0].split(':')[1].split()]
# index = 3
# for i in range(7):
#     mapping, index = map_object_to_another(lines, index)
#     mappings.append(mapping)
# print(mappings)
# lowest = max(seeds)
# for seed in seeds:
#     for mapping in mappings:
#         if seed in mapping:
#             seed = mapping[seed]
#     if seed < lowest:
#         lowest = seed
# print(lowest)
    
def map_single_object_to_another(lines, index, object):
    while index < len(lines) - 1 and lines[index] != '' :
        dest, source, _range = lines[index].split()
        dest, source, _range = int(dest), int(source), int(_range)
        if source <= object <= source + _range:
            return (dest + object - source), put_index_to_next(lines, index)
        index += 1
    return object, index + 2

def put_index_to_next(lines, index):
    while index < len(lines) - 1 and lines[index] != '':
        index += 1
    return index + 2

lines = read_input(current,Choice.REAL).read().split('\n')
seeds = [int(x) for x in lines[0].split(':')[1].split()]
lowest = max(seeds)
for seed in seeds:
    index = 3
    for i in range(7):
        seed, index = map_single_object_to_another(lines, index, seed)
    if seed < lowest:
        lowest = seed
print(lowest)

# Part 2
lines = read_input(current,Choice.TEST).read().split('\n')
seeds = [int(x) for x in lines[0].split(':')[1].split()]
lowest = max(seeds)
for seedI in range(0, len(seeds), 2):
    for seedJ in range(seeds[seedI], seeds[seedI] + seeds[seedI + 1]):
        index = 3
        for i in range(7):
            seedJ, index = map_single_object_to_another(lines, index, seedJ)
        if seedJ < lowest:
            lowest = seedJ
print(lowest)