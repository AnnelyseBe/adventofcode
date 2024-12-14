from utils.execution_timer import ExecutionTimer
from utils.array_helper import ArrayHelper
from collections import namedtuple, Counter
import numpy as np
from pathlib import Path
import re


# Define the base directory relative to the current script's location
BASE_DIR = Path(__file__).parent  # Path to the current script's folder

# Define paths to your input files dynamically
INPUT = BASE_DIR / 'input'
TEST_INPUT = BASE_DIR / 'input_test'
TEST_INPUT_B = BASE_DIR / 'input_test_B'


def transform_input(inputlocation):
    with open(inputlocation) as file:
        content = [list(line) for line in file.read().splitlines()]
        map = np.array(content)
        return map

def next_coordinates(direction, position_row, position_column):
    match direction: 
        case "NORTH": 
            return position_row - 1, position_column
        case "EAST": 
            return position_row, position_column + 1
        case "WEST": 
            return position_row, position_column - 1
        case "SOUTH": 
            return position_row + 1, position_column
        case _ : 
            return position_row, position_column
        
def turn(direction):
    match direction: 
        case "NORTH": 
            return "EAST"
        case "EAST": 
            return "SOUTH"
        case "SOUTH": 
            return "WEST"
        case "WEST": 
            return "NORTH"
        case _ : 
            return direction

        
    
def route(map):
    NORTH = '^'
    EAST = '>' 
    SOUTH = 'v'
    WEST = '<'
    
    rowcount, columncount = map.shape
    
    in_infinite_loop = False
    in_map = True
    position_row, position_column = ArrayHelper.find_item_position_in_2d(map, NORTH)

    direction = 'NORTH'
    
    direction_and_location = set()
    diffrent_movement_count = 0
    
    while(in_map and not in_infinite_loop):
        # evaluate next position
        next_position_row, next_position_column = next_coordinates(direction, position_row, position_column)

        # evaluate 
        if (next_position_row < 0 or next_position_row >= rowcount or next_position_column <0 or next_position_column >= columncount):  # out of bound
            map[position_row, position_column] = 'X'
            in_map = False
        elif (map[next_position_row, next_position_column] == '#'): # turn 
            direction = turn(direction)
        elif (map[next_position_row, next_position_column] == 'O'): # turn 
            direction = turn(direction)
        elif (map[next_position_row, next_position_column] != '#'):  # valid step
            map[position_row, position_column] = 'X'
            direction_and_location.add((direction, next_position_row, next_position_column))
            if (len(direction_and_location) > diffrent_movement_count): # not yet in a loop, never run this place in this direction
                position_row, position_column = next_position_row, next_position_column
            else:
                in_infinite_loop = True
        
        diffrent_movement_count = len(direction_and_location)
        
    return map, in_infinite_loop

            


print("=================== part A ===================")
with ExecutionTimer():
    map = transform_input(INPUT)
    print(map)
    route(map)
    print(map)
    count_X = np.count_nonzero(map == 'X')
    print(f"{count_X}")

# 5461
# Execution time: 0 hours, 0 minutes, 0 seconds, 28.0315 milliseconds
print("=================== part B ===================")
with ExecutionTimer():
    map_original = transform_input(INPUT)   
    
    rowcount, columncount = map_original.shape
    counter_infinite_loops = 0
    
    for rowindex in range(rowcount):
        for columnindex in range(columncount):
            if (map_original[rowindex][columnindex] == '.'):
                map_obstacle = map_original.copy()
                map_obstacle[rowindex][columnindex] = 'O'
                _ , is_infinite = route(map_obstacle)
                if is_infinite:
                    counter_infinite_loops += 1
                
    print(counter_infinite_loops)
    
# 1836
# Execution time: 0 hours, 2 minutes, 31 seconds, 664.7127 milliseconds

    












