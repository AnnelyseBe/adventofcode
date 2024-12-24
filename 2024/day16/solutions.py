from utils.execution_timer import ExecutionTimer
from utils.array_helper import ArrayHelper
from collections import namedtuple, Counter
import numpy as np
from pathlib import Path
import re
from itertools import product 
import copy
import math
import sys  


# Define the base directory relative to the current script's location
BASE_DIR = Path(__file__).parent  # Path to the current script's folder

# Define paths to your input files dynamically
INPUT = BASE_DIR / 'input'
TEST_INPUT_A = BASE_DIR / 'input_test_A'
TEST_INPUT_B = BASE_DIR / 'input_test_B'
TEST_INPUT_C = BASE_DIR / 'input_test_C'

START = 'S'
END = 'E'
EMPTY = '.'
WALL = '#'


def transform_input(inputlocation):
    with open(inputlocation) as file:
        maze = np.array([list(row) for row in file.read().splitlines()])
        return maze
    

def turn_posibilities(direction):
    posibilities = []
    
    if direction == 'n':
        posibilities.extend([("n", 0), ("e", 1), ("w", 1)])
    elif direction == 'e':
        posibilities.extend([("e", 0), ("n", 1), ("s", 1)])
    elif direction == 's':
        posibilities.extend([("s", 0), ("e", 1), ("w", 1)])
    elif direction == 'w':
        posibilities.extend([("w", 0), ("n", 1), ("s", 1)])
    
    # print(f"posibilities: {posibilities}")
    return posibilities
    
def move(position, direction, route, turn_count, step_count, visited):
    if (position, direction) in visited:
        return
    visited.add((position, direction))
    
    print(f"start from current position:{position} with direction:{direction}, afgelegde route:{route}, turn_count:{turn_count}, step_count:{step_count}")
    for new_direction, turns in turn_posibilities(direction):        
        turn_count = turn_count + turns
        next_place = ArrayHelper.valid_neighbour_coordinates_and_value(maze, new_direction, position)
        print(f"     current position:{position}, turn in direction:{new_direction} towards {next_place[0]}")
        if (next_place):
            next_pos, next_val = next_place
            if (next_val == EMPTY):
                step_count += 1
                route += new_direction
                print(f"          MOVE from current position:{position} to next position: {next_pos}. Route: {route}, turn_count:{turn_count}, step_count:{step_count}")
                move(next_pos, new_direction, route, turn_count, step_count, visited)
            elif (next_val == END):
                step_count += 1
                route += new_direction
                print(f"          END from current position:{position} to END position: {next_pos}. Result: {step_count + 1000 * turn_count}, route: {route}, turn_count:{turn_count}, step_count:{step_count}")
                routes.append((step_count + 1000 * turn_count, step_count, turn_count, route))
                return
            elif (next_val == WALL):
                print(f"          STOP current position:{position}, no move because {next_pos} = wall ")
                continue
            else:
                print(f"AIAIAI")
                continue
        else:
            print(f"          point not valid")
            continue


def rank_route(route):
    return route[0]
                


print("=================== part A ===================")
with ExecutionTimer():
    sys.setrecursionlimit(100000)
    maze = transform_input(TEST_INPUT_A)
    ArrayHelper.print_2d_array_string_values(maze)
    
    start_position = ArrayHelper.find_next_coordinates_that_contain(maze, START)
    routes = []
    visited = set()
    
    move(start_position, 'n', '', 0, 0, visited)
    
    sorted_routes = sorted(routes, key=rank_route)
    print(sorted_routes[0])
    
    
# TEST_INPUT_A: 7036
# TEST_INPUT_B: 11048


    

    
print("=================== part B ===================")
with ExecutionTimer():
    transform_input(TEST_INPUT_A)
    print("todo")
    
    

# Recursie heeft een limiet van 999 (denk ik). Ter vergroten met import sys en sys.setrecursionlimit(100000).
# Dit is een grafen probleem. Er zijn verschillende manieren om dit op te lossen
    # Dijkstra algoritme: 
    #   https://www.reddit.com/r/adventofcode/comments/1hiicuy/2024_day_16_part_1python/?share_id=caugEmLv-bLeD2TQzLQS7&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=3
    #   https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python
    # BFS (breadth First Search) en DFS
    
# Wat in deze oplossing mis loopt, is dat hij niet alle routes lijkt te nemen. Op een bepaald moment zit hij fout en gaat hij niet genoeg stappen terug.
    

    












