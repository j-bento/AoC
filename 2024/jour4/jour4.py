import sys
import os

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

from helper import *
# returns the number of times the word "XMAS" appears in the matrix at the given position
def check_pos_p1(matrix:list, i:int, j:int) -> int:
    res = 0
    for idxI in [-3, 0, 3]: 
        for idxJ in [-3, 0, 3]:
            # if the indexes aren't out of bounds, we check for the word "XMAS" at the given position
            if not (i + idxI < 0 or i + idxI >= len(matrix)) and not (j + idxJ < 0 or j + idxJ >= len(matrix[i])) and not (idxI == 0 and idxJ == 0):
                MindexI = i + 1 * (-1 if idxI < 0 else (1 if idxI > 0 else 0))
                MindexJ = j + 1 * (-1 if idxJ < 0 else (1 if idxJ > 0 else 0))
                AindexI = i + 2 * (-1 if idxI < 0 else (1 if idxI > 0 else 0))
                AindexJ = j + 2 * (-1 if idxJ < 0 else (1 if idxJ > 0 else 0))
                if matrix[i][j] == 'X' and matrix[MindexI][MindexJ] == 'M' and matrix[AindexI][AindexJ] == 'A' and matrix[i + idxI][j + idxJ] == 'S':
                    res += 1
    return res

# returns the number of times the word "XMAS" appears in the matrix at the given position
def check_pos_p2(matrix:list, i:int, j:int) -> int:
    res = 0
    # if the indexes aren't out of bounds, we check for the word "XMAS" at the given position
    if not (i + 2 >= len(matrix)) and not (j + 2 >= len(matrix[i])):
        if check_nb_mas(matrix, i, j) >= 2:
            res += 1
    return res    
            
# checks the number of 'MAS' in a 3x3 matrix
def check_nb_mas(matrix:list, i:int, j:int) -> int:
    res = 0
    if matrix[i][j] == 'M' and matrix[i + 1][j + 1] == 'A' and matrix[i + 2][j + 2] == 'S':
        res += 1
    if matrix[i][j] == 'S' and matrix[i + 1][j + 1] == 'A' and matrix[i + 2][j + 2] == 'M':
        res += 1
    if matrix[i + 2][j] == 'M' and matrix[i + 1][j + 1] == 'A' and matrix[i][j + 2] == 'S':
        res += 1
    if matrix[i + 2][j] == 'S' and matrix[i + 1][j + 1] == 'A' and matrix[i][j + 2] == 'M':
        res += 1
    return res
    
# Part 1
file = read_input(current, Choice.REAL)
letters_matrix = [line.strip() for line in file.readlines()]
res = 0
for i in range(len(letters_matrix)):
    for j in range(len(letters_matrix[0])):
        res += check_pos_p1(letters_matrix, i, j)
print(res)

# Part 2
file = read_input(current, Choice.REAL)
letters_matrix = [line.strip() for line in file.readlines()]
res = 0
for i in range(len(letters_matrix)):
    for j in range(len(letters_matrix[0])):
        res += check_pos_p2(letters_matrix, i, j)
print(res)