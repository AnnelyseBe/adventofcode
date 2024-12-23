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

def move_box_line(first_box_pos, direction, after_boxes_pos):
    warehouse_old_sit = warehouse.copy()
    first_box_pos_row, first_box_pos_col = first_box_pos
    after_box_pos_row, after_box_pos_col = after_boxes_pos
    
    dir_cor = 1 if (direction == '>' or direction == 'v') else -1
    
    if (direction == '>' or direction == '<'): # horizontal move
        # print(f"         horizontal move boxes from {first_box_pos} to {after_boxes_pos}")
        for col in range(first_box_pos_col, after_box_pos_col + dir_cor, dir_cor):
            warehouse[first_box_pos_row][col] = warehouse_old_sit[first_box_pos_row][col - dir_cor]
            # print(f"         {warehouse_old_sit[first_box_pos_row][col - dir_cor]} moved from ({first_box_pos_row},{col - dir_cor}) to ({first_box_pos_row},{col})")
    elif (direction == 'v' or direction == '^'): # vertical move 
        # print(f"         vertical move boxes from {first_box_pos} to {after_boxes_pos}")
        for row in range(first_box_pos_row, after_box_pos_row + dir_cor, dir_cor):
            warehouse[row][first_box_pos_col] = warehouse_old_sit[row - dir_cor][first_box_pos_col]
            # print(f"         {warehouse_old_sit[row - dir_cor][first_box_pos_col]} moved from ({row - dir_cor},{first_box_pos_col}) to ({row},{first_box_pos_col})")
        

def other_box_part_position(position):
    row, column = position
    if (warehouse[position] == BOX_LEFT):
        return(row, column + 1)
    else:
        return(row, column - 1)
    
def find_impacted_boxes(first_box_pos, direction):
    first_box_pos_row, _ = first_box_pos
    dir_cor = 1 if (direction == '>' or direction == 'v') else -1
    impacted_positions = {}
    move_possible = True
    impacted_on_row = True
    
    
    row = first_box_pos_row
    
    
    while (impacted_on_row): # zolang we op de volgende rij nog items vinden
        impacted_on_row = []
        
        if (row == first_box_pos_row): # eerste rij toevoegen aan geïmpacteerden
            impacted_on_row.append(first_box_pos)
            impacted_on_row.append(other_box_part_position(first_box_pos))
            # print(f"               first row: {row} impacted: {impacted_on_row}")
            impacted_positions[row] = set(impacted_on_row)
        else:    # row bekijken tov geïmpacteerden van de vorige rij
            for pos_impacted_prev_row in impacted_positions[row - dir_cor]:
                _, col_impacted_prev_row = pos_impacted_prev_row
                pos_eval = row, col_impacted_prev_row
                val_eval = warehouse[pos_eval]
                
                if (val_eval == WALL):
                    return False, None
                elif (val_eval == BOX_LEFT or val_eval == BOX_RIGHT):
                    impacted_on_row.append(pos_eval)
                    impacted_on_row.append(other_box_part_position(pos_eval))
            # print(f"               row: {row} impacted: {impacted_on_row}")
            impacted_positions[row] = set(impacted_on_row)
              
        row += dir_cor
        # print(f"               new row: {row}")
    return move_possible, impacted_positions
        
def move_impacted_boxes(impacted_boxes, direction):
    warehouse_old = warehouse.copy()
    dir_cor = 1 if direction == 'v' else -1
    
    for row in sorted(impacted_boxes, reverse=(True if dir_cor == 1 else False)):        
        for _, col in impacted_boxes[row]:
            warehouse[row + dir_cor][col] = warehouse_old[row][col] 
            warehouse[row][col] = EMPTY
            
            
            

def move_robot_from_to(start_position, next_pos):
    warehouse[start_position] = EMPTY
    warehouse[next_pos] = ROBOT
    return next_pos
    
def move(start_position, warehouse, direction):
    next_pos, next_value = ArrayHelper.valid_neighbour_coordinates_and_value(warehouse, direction, start_position)
    
    is_horizontal = (direction == '>' or direction == '<')
    is_big_box = (next_value == BOX_LEFT or next_value == BOX_RIGHT)
    # print(f"    next position {next_pos} is {next_value} ...")
    
    if (next_value == EMPTY):
        # print(f"    next position {next_pos} is EMPTY, move")
        return move_robot_from_to(start_position, next_pos)
    elif (next_value == WALL):
        # print(f"    next position {next_pos} is WALL, no move")
        return start_position
    elif (next_value == BOX or (is_horizontal and is_big_box)):   
        # print(f"    next position {next_pos} is BOX, is_horizontal: {is_horizontal}, is_big_box: {is_big_box}")    
        after_boxes_pos, after_boxes_value = find_next_non_box_value(start_position, warehouse, direction)      
        if (after_boxes_value == WALL):
            # print(f"    can not move box")
            return start_position
        elif (after_boxes_value == EMPTY):
            # print(f"    box will be moved")
            warehouse = move_box_line(next_pos, direction, after_boxes_pos)
            return move_robot_from_to(start_position, next_pos)
    elif (not is_horizontal and is_big_box):
        move_possible, impacted_boxes = find_impacted_boxes(next_pos, direction)
        
        if(move_possible):
            move_impacted_boxes(impacted_boxes, direction)
            return move_robot_from_to(start_position, next_pos)
        else:
            # print(f"    can not move box")
            return start_position
            
def find_next_non_box_value(start_position, warehouse, direction):
    next_value = BOX
    while(next_value == BOX or next_value == BOX_LEFT or next_value == BOX_RIGHT):
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
    
# TEST_INPUT_A: 2028
# TEST_INPUT_B: 10092
# 1486930
# Execution time: 0 hours, 0 minutes, 0 seconds, 89.4109 milliseconds
        
        
    

    

    
print("=================== part B ===================")
with ExecutionTimer():
    warehouse, directions = transform_input(INPUT)
    warehouse = transform_part_B(warehouse)
    # ArrayHelper.print_2d_array_string_values(warehouse)

    
    box_GPS_sum = 0
    start_position = ArrayHelper.find_next_coordinates_that_contain(warehouse, ROBOT)
    
    # ArrayHelper.print_2d_array_string_values(warehouse)
    

    for i, direction in enumerate(directions):
        # print(f"direction {i}: {direction}")
        start_position = move(start_position, warehouse, direction)
        # ArrayHelper.print_2d_array_string_values(warehouse)
        # print(f"robot position: {start_position}")
        
    for row in range(warehouse.shape[0]):
        for col in range(warehouse.shape[1]):
            if (warehouse[row][col] == BOX_LEFT):
                box_GPS_sum += 100 * row + col
                
    print(box_GPS_sum)
    
    
# TEST_INPUT_A: 
# TEST_INPUT_B: 9021
# 1492011
# Execution time: 0 hours, 0 minutes, 0 seconds, 71.7967 milliseconds

    












