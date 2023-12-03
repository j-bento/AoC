import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from helper import *

# Part 1
file = read_input(current, Choice.REAL)
max_red_cubes = 12
max_green_cubes = 13
max_blue_cubes = 14
_sum = 0
for line in file:
    game_id, sets = line.split(':')

    for set in sets.split(';'):
        red_cubes = 0
        green_cubes = 0
        blue_cubes = 0
        for pick in set.split(','):
            amount, color = pick.strip().split(' ')
            if color == 'red':
                red_cubes += int(amount)
            elif color == 'green':
                green_cubes += int(amount)
            elif color == 'blue':
                blue_cubes += int(amount)
        impossible = red_cubes > max_red_cubes or green_cubes > max_green_cubes or blue_cubes > max_blue_cubes
        if impossible:
            break
    if not impossible:
        _sum += int(game_id.split(' ')[1])
print(_sum)

# Part 2
file = read_input(current, Choice.REAL)
_sum = 0
for line in file:
    game_id, sets = line.split(':')
    min_red_cubes = 0
    min_green_cubes = 0
    min_blue_cubes = 0

    for set in sets.split(';'):
        for pick in set.split(','):
            amount, color = pick.strip().split(' ')
            if color == 'red':
                if int(amount) > min_red_cubes:
                    min_red_cubes = int(amount)
            elif color == 'green':
                if int(amount) > min_green_cubes:
                    min_green_cubes = int(amount)
            elif color == 'blue':
                if int(amount) > min_blue_cubes:
                    min_blue_cubes = int(amount)
    _sum += min_red_cubes * min_green_cubes * min_blue_cubes
    print(min_red_cubes, min_green_cubes, min_blue_cubes)
print(_sum)