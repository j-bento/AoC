import sys
import os

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

from helper import *
def init_guard_pos(matrix):
    guardPos = (0, 0)
    # find the guard position
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '^':
                guardPos = (i, j)
                break
    return guardPos

def check_with_obstacle(matrix, obstacle_to_add):
    global guardPos
    # add the new obstacle
    matrix[obstacle_to_add[0]] = matrix[obstacle_to_add[0]][:obstacle_to_add[1]] + '#' + matrix[obstacle_to_add[0]][obstacle_to_add[1] + 1:]
    # up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dIdx = 0
    currentDir = directions[dIdx]
    try:
        # slightly optimized version of the main loop from part 1
        while True:
            if any(pos < 0 or pos >= len(matrix) for pos in guardPos):
                return 0
            if matrix[guardPos[0] + currentDir[0]][guardPos[1] + currentDir[1]] == '#':
                dIdx = (dIdx + 1) % 4
                currentDir = directions[dIdx]
            else:
                guardPos = (guardPos[0] + currentDir[0], guardPos[1] + currentDir[1])
                if matrix[guardPos[0]][guardPos[1]] == str(dIdx): # same direction as the guard === the guard has made a loop
                    return 1
                else:
                    matrix[guardPos[0]] = matrix[guardPos[0]][:guardPos[1]] + str(dIdx) + matrix[guardPos[0]][guardPos[1] + 1:]
    except IndexError: # the guard has reached the end of the matrix without making a loop
        return 0
    
# Part 1
file = read_input(current, Choice.REAL)
matrix = [line.strip("\n") for line in file.readlines()]
guardPos = init_guard_pos(matrix)
guardDir = '^'

try:
    while True:
        matrix[guardPos[0]] = matrix[guardPos[0]][:guardPos[1]] + 'X' + matrix[guardPos[0]][guardPos[1] + 1:]
        # check for the next direction
        if guardDir == '^':
            if matrix[guardPos[0] - 1][guardPos[1]] == '#':
                guardDir = '>'
            else:
                guardPos = (guardPos[0] - 1, guardPos[1])
        elif guardDir == '>':
            if matrix[guardPos[0]][guardPos[1] + 1] == '#':
                guardDir = 'v'
            else:
                guardPos = (guardPos[0], guardPos[1] + 1)
        elif guardDir == 'v':
            if matrix[guardPos[0] + 1][guardPos[1]] == '#':
                guardDir = '<'
            else:
                guardPos = (guardPos[0] + 1, guardPos[1])
        elif guardDir == '<':
            if matrix[guardPos[0]][guardPos[1] - 1] == '#':
                guardDir = '^'
            else:
                guardPos = (guardPos[0], guardPos[1] - 1)
except IndexError:
    print(''.join(matrix).count('X'))

# Part 2
file = read_input(current, Choice.REAL)
matrix = [line.strip("\n") for line in file.readlines()]

guardPos = init_guard_pos(matrix)
guardX = guardPos[0]
guardY = guardPos[1]
res = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '.':
            guardPos = (guardX, guardY)
            res += check_with_obstacle(matrix[:], (i, j))
print(res)