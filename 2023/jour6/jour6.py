import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from helper import *

# Part 1
lines = read_input(current,Choice.REAL).read().split('\n')
times = [int(x) for x in lines[0].split(':')[1].split()]
distances_to_beat = [int(x) for x in lines[1].split(':')[1].split()]

def calculate_distance(time, press_duration):
    return (time - press_duration) * press_duration

times_nb_ways = []
for i, time in enumerate(times):
    nb_ways = 0
    for j in range(1, time):
        if calculate_distance(time, j) > distances_to_beat[i]:
            nb_ways += 1
    times_nb_ways.append(nb_ways)
            
print(prod(times_nb_ways))

# Part 2
lines = read_input(current,Choice.REAL).read().split('\n')
time = int(''.join(str(x) for x in lines[0].split(':')[1].split()))
distance_to_beat = int(''.join(str(x) for x in lines[1].split(':')[1].split()))

nb_ways = 0
for i in range(1, time):
    if calculate_distance(time, i) > distance_to_beat:
        nb_ways += 1
print(nb_ways)