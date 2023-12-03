import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from helper import *

# Part 1
file = read_input(current, Choice.REAL)
sum = 0
for line in file:
    currentLineValue = ""
    for char in line:
        # check if char is a number
        if char.isdigit():
            currentLineValue += char
    currentLineValue = int(currentLineValue[0] + currentLineValue[-1])
    sum += currentLineValue
print(sum)

# Part 2
file = read_input(current, Choice.REAL)
sum = 0
values = {}
values["one"] = 1
values["two"] = 2
values["three"] = 3
values["four"] = 4
values["five"] = 5
values["six"] = 6
values["seven"] = 7
values["eight"] = 8
values["nine"] = 9
for line in file:
    currentLineValue = ""
    for i, char in enumerate(line):
        # check if char is a number 
        if char.isdigit():
            currentLineValue += char
        if line[i:i+3] in values:
            currentLineValue += str(values[line[i:i+3]])
        if line[i:i+4] in values:
            currentLineValue += str(values[line[i:i+4]])
        if line[i:i+5] in values:
            currentLineValue += str(values[line[i:i+5]])
    currentLineValue = int(currentLineValue[0] + currentLineValue[-1])
    sum += currentLineValue
print(sum)