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

# todo ... warehouse moeten we eigenlijk niet meegeven
def move_box_line(first_box_pos, direction, after_boxes_pos, warehouse): # move all inclusief robot
    warehouse_old_sit = warehouse.copy()
    first_box_pos_row, first_box_pos_col = first_box_pos
    after_box_pos_row, after_box_pos_col = after_boxes_pos
    
    dir_cor = 1 if (direction == '>' or direction == 'v') else -1
    
    if (direction == '>' or direction == '<'): # horizontal move
        print(f"         horizontal move boxes from {first_box_pos} to {after_boxes_pos}")
        for col in range(first_box_pos_col, after_box_pos_col + dir_cor, dir_cor):
            warehouse[first_box_pos_row][col] = warehouse_old_sit[first_box_pos_row][col - dir_cor]
            print(f"         {warehouse_old_sit[first_box_pos_row][col - dir_cor]} moved from ({first_box_pos_row},{col - dir_cor}) to ({first_box_pos_row},{col})")
    elif (direction == 'v' or direction == '^'): # vertical move 
        print(f"         vertical move boxes from {first_box_pos} to {after_boxes_pos}")
        for row in range(first_box_pos_row, after_box_pos_row + dir_cor, dir_cor):
            warehouse[row][first_box_pos_col] = warehouse_old_sit[row - dir_cor][first_box_pos_col]
            print(f"         {warehouse_old_sit[row - dir_cor][first_box_pos_col]} moved from ({row - dir_cor},{first_box_pos_col}) to ({row},{first_box_pos_col})")
            
    return warehouse # todo eigenlijk niet nodig
    
def move(start_position, warehouse, direction):
    next_pos, next_value = ArrayHelper.valid_neighbour_coordinates_and_value(warehouse, direction, start_position)
    print(f"    next position {next_pos} is {next_value} ....")
    
    if (next_value == EMPTY):
        print(f"    next position {next_pos} is EMPTY")
        warehouse[start_position] = EMPTY
        warehouse[next_pos] = ROBOT
        return next_pos
    elif (next_value == WALL):
        print(f"    next position {next_pos} is WALL")
        return start_position
    elif (next_value == BOX):       
        after_boxes_pos, after_boxes_value = find_next_non_box_value(start_position, warehouse, direction)      
        if (after_boxes_value == WALL):
            print(f"    can not move box")
            return start_position
        elif (after_boxes_value == EMPTY):
            warehouse = move_box_line(next_pos, direction, after_boxes_pos, warehouse)
            warehouse[start_position] = EMPTY # robot space becomes empty
            return next_pos
    # elif ((direction == '>' or direction == '<') and (next_value == 'BOX_LEFT' or next_value == 'BOX_RIGHT')): # horizontal big boxes
    #      after_boxes_pos, after_boxes_value = find_next_non_box_value(start_position, warehouse, direction) 
        
        

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
    warehouse, directions = transform_input(TEST_INPUT_A)
    # print(directions)
    
    box_GPS_sum = 0
    start_position = ArrayHelper.find_next_coordinates_that_contain(warehouse, ROBOT)
    
    print(warehouse)
    
    for i, direction in enumerate(directions):
        print(f"direction {i}: {direction}")
        start_position = move(start_position, warehouse, direction)
        ArrayHelper.print_2d_array_string_values(warehouse)
        print(f"robot position: {start_position}")
        
    for row in range(warehouse.shape[0]):
        for col in range(warehouse.shape[1]):
            if (warehouse[row][col] == BOX):
                box_GPS_sum += 100 * row + col
                
    print(box_GPS_sum)
    
# TEST_INPUT_A: 2028
# TEST_INPUT_B: 10092
        
        
    

    

    
print("=================== part B ===================")
with ExecutionTimer():
    warehouse, directions = transform_input(TEST_INPUT_A)
    warehouse = transform_part_B(warehouse)
    ArrayHelper.print_2d_array_string_values(warehouse)
    
    # todo, nu nog de bewegingen aanpassen
    
    # for i, direction in enumerate(directions):
    #     # print(f"direction {i}: {direction}")
    #     start_position = move(start_position, warehouse, direction)
    #     # ArrayHelper.print_2d_array_string_values(warehouse)
    #     # print(f"robot position: {start_position}")

    












