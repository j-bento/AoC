import sys
import os
import re

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

from helper import *

# Part 1
# file = read_input(current, Choice.REAL)
# lines = ''.join(file.readlines())
# res = sum([int(i) * int(j) for (i, j) in re.findall(r"mul\(([0-9]+),([0-9]+)\)", lines)])
# print(res)

# single line version
print(sum([int(i) * int(j) for (i, j) in re.findall(r"mul\(([0-9]+),([0-9]+)\)", ''.join(read_input(current, Choice.REAL).readlines()))]))

# Part 2
file = read_input(current, Choice.REAL)
lines = ''.join(file.readlines())
filtered_memory = ""
enabled = True
prevIdx , idx = 0, 0
# build the string on which we'll apply our previous regex
while idx < len(lines):
    try:
        if enabled:
            # look for the next don't
            idx = lines.index("don't()", prevIdx)
            filtered_memory += lines[prevIdx:idx]
            prevIdx = idx
            enabled = False
        else:
            # look for the next do
            idx = lines.index("do()", prevIdx)
            prevIdx = idx
            enabled = True
    except ValueError:
        if enabled: # add the remaining memory data if the last block was a do()
            filtered_memory += lines[prevIdx:]
        idx = len(lines)

# apply the regex to the filtered memory
res = sum([int(i) * int(j) for (i, j) in re.findall(r"mul\(([0-9]+),([0-9]+)\)", filtered_memory)])
print(res)