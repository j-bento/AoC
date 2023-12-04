import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from helper import *

# Part 1
games = read_input(current, Choice.REAL).read().split('\n')
_sum = 0
for line in games:
    count = -1
    winning_numbers, numbers = line.split(':')[1].split('|')
    winning_numbers, numbers = winning_numbers.split(), numbers.split()
    for number in numbers:
        if number in winning_numbers:
            count += 1
    if count >= 0:
        _sum += pow(2, count)
print(_sum)

# Part 2
def count_points(game):
    game_id, game_data = game.split(':')
    winning_numbers, numbers = game_data.split('|')
    numbers = numbers.split()
    winning_numbers = set(winning_numbers.split())
    count = 0
    for number in numbers:
        if number in winning_numbers:
            count += 1
    return count

games = read_input(current, Choice.REAL).read().split('\n')
cache = {}
counter = 0
for game in games:
    game_id, game_data = game.split(':')
    game_id = int(game_id.strip('Card '))
    if game_id in cache:
        games += cache[game_id]
    else:
        winning_numbers, numbers = line.split(':')[1].split('|')
        winning_numbers, numbers = winning_numbers.split(), numbers.split()
        points = count_points(game)
        to_add = []
        for i in range(points):
            to_add.append(games[game_id + i])
        cache[game_id] = to_add
        games += to_add
    counter += 1
print(counter)