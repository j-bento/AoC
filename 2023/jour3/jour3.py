import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from helper import *

# Part 1
file = read_input(current, Choice.REAL).read().split('\n')
def get_numbers(i, j):
    numbers = []
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if not (k == i and l == j):
                if file[k][l].isdigit():
                    start = l
                    while start > 0 and file[k][start-1].isdigit() :
                        start -= 1
                    end = start + 1
                    while end < len(file[k]) and file[k][end].isdigit():
                        end += 1
                    if not int(file[k][start:end]) in numbers:
                        numbers.append(int(file[k][start:end]))
    return numbers

_sum = 0
for i, line in enumerate(file):
    for j, char in enumerate(line.strip()):
        if not char == '.' and not char.isdigit():
            _sum += sum(get_numbers(i, j))
print(_sum)

# Part 2
file = read_input(current, Choice.REAL).read().split('\n')
_sum = 0
for i, line in enumerate(file):
    for j, char in enumerate(line.strip()):
        if char == '*':
            numbers = get_numbers(i, j)
            if len(numbers) > 1:
                _sum += prod(numbers)
print(_sum)