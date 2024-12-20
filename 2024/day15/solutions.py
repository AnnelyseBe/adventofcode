from utils.execution_timer import ExecutionTimer
from utils.array_helper import ArrayHelper
from collections import namedtuple, Counter
import numpy as np
from pathlib import Path
import re
from itertools import product 
import copy
import math
import typing


# Define the base directory relative to the current script's location
BASE_DIR = Path(__file__).parent  # Path to the current script's folder

# Define paths to your input files dynamically
INPUT = BASE_DIR / 'input'
TEST_INPUT_A = BASE_DIR / 'input_test_A'
TEST_INPUT_B = BASE_DIR / 'input_test_B'
TEST_INPUT_C = BASE_DIR / 'input_test_C'

ROBOT = '@'
EMPTY = '.'
WALL = '#'
BOX = 'O'
BOX_LEFT = '['
BOX_RIGHT = ']'


def transform_input(inputlocation):
    with open(inputlocation) as file:
        warehouse, directions_lines = file.read().split("\n\n")
        directions = []
        
        for row in directions_lines.splitlines():
            directions.extend(row)
            
        warehouse = np.array([[char for char in row] for row in warehouse.split()])
        
        return warehouse, directions
    
def transform_part_B(warehouse):
    new_warehouse = np.repeat(warehouse, 2, axis=1)
    rows, cols = new_warehouse.shape
    
    for row in range(rows):
        for col in range(cols):
            if (new_warehouse[row, col] == BOX):
                new_warehouse[row,col] = BOX_LEFT
                new_warehouse[row,col+1] = BOX_RIGHT
            elif (new_warehouse[row, col] == ROBOT):
                new_warehouse[row,col+1] = EMPTY
                
    return new_warehouse
                
                
    
    
def move(start_position, warehouse, direction):
    next_pos, next_value = ArrayHelper.valid_neighbour_coordinates_and_value(warehouse, direction, start_position)
    # print(f"    next position {next_pos} is {next_value} ....")
    
    if (next_value == EMPTY):
        # print(f"    next position {next_pos} is EMPTY")
        warehouse[start_position] = EMPTY
        warehouse[next_pos] = ROBOT
        return next_pos
    elif (next_value == WALL):
        # print(f"    next position {next_pos} is WALL")
        return start_position
    elif (next_value == BOX):       
        after_boxes_pos, after_boxes_value = find_next_non_box_value(start_position, warehouse, direction)      
        if (after_boxes_value == WALL):
            # print(f"    can not move box")
            return start_position
        elif (after_boxes_value == EMPTY):
            warehouse[after_boxes_pos] = BOX
            warehouse[start_position] = EMPTY
            warehouse[next_pos] = ROBOT
            # print(f"    box moved from {next_pos} to {after_boxes_pos}")
            return next_pos

    else:
        print(f"!!!!!! next pos: {next_pos}, next val: {next_value}")
            
def find_next_non_box_value(start_position, warehouse, direction):
    next_value = BOX
    while(next_value == BOX):
        next_pos, next_value = ArrayHelper.valid_neighbour_coordinates_and_value(warehouse, direction, start_position)
        start_position = next_pos
        # print(f"next pos {next_pos}: {next_value}")
    return next_pos, next_value
        
    

print("=================== part A ===================")
with ExecutionTimer():
    warehouse, directions = transform_input(INPUT)
    # print(directions)
    
    box_GPS_sum = 0
    start_position = ArrayHelper.find_next_coordinates_that_contain(warehouse, ROBOT)
    
    # print(warehouse)
    
    for i, direction in enumerate(directions):
        # print(f"direction {i}: {direction}")
        start_position = move(start_position, warehouse, direction)
        # ArrayHelper.print_2d_array_string_values(warehouse)
        # print(f"robot position: {start_position}")
        
    for row in range(warehouse.shape[0]):
        for col in range(warehouse.shape[1]):
            if (warehouse[row][col] == BOX):
                box_GPS_sum += 100 * row + col
                
    print(box_GPS_sum)
        
        
    

    

    
print("=================== part B ===================")
with ExecutionTimer():
    warehouse, directions = transform_input(TEST_INPUT_A)
    warehouse = transform_part_B(warehouse)
    ArrayHelper.print_2d_array_string_values(warehouse)
    
    # todo, nu nog de bewegingen aanpassen

    












