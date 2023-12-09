import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from helper import *
from math import lcm

# Part 1
def go_through_directions(currentNode : str, _count : int, endChar : str):
    for direction in directions:
        if direction == 'L':
            currentNode = nodes[currentNode][0]
        else:
            currentNode = nodes[currentNode][1]
        _count += 1
        if currentNode.endswith(endChar):
            return currentNode, _count
    return currentNode, _count

directions, lines = read_input(current,Choice.REAL).read().split('\n\n')
nodes = {}
for line in lines.split('\n'):
    line = line.split(' = ')
    nodes[line[0]] = line[1][1:-1].split(', ')

_count = 0
currentNode = "AAA"
endChar = "ZZZ"
while not currentNode.endswith(endChar):
    currentNode, _count = go_through_directions(currentNode, _count, endChar)
print(_count)

# Part 2
currentNodes = []
for key in nodes:
    if key[-1] == 'A':
        currentNodes.append(key)

_counts = []
endChar = 'Z'
for currentNode in currentNodes:
    _count = 0
    while not currentNode.endswith(endChar):
        currentNode, _count = go_through_directions(currentNode, _count, endChar)
    _counts.append(_count)
    
print(lcm(*_counts))