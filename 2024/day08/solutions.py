from utils.execution_timer import ExecutionTimer
from utils.array_helper import ArrayHelper
from collections import namedtuple, Counter
import numpy as np
from pathlib import Path
import re
from itertools import product 
import copy
import math


# Define the base directory relative to the current script's location
BASE_DIR = Path(__file__).parent  # Path to the current script's folder

# Define paths to your input files dynamically
INPUT = BASE_DIR / 'input'
TEST_INPUT = BASE_DIR / 'input_test'

Coordinates = namedtuple('Coordinates', ['row', 'column'])


def transform_input(inputlocation):
    with open(inputlocation) as file:
        content = [list(line) for line in file.read().splitlines()]
        map = np.array(content, dtype='<U2') #standaard <U1, maar dan kunnen we er geen # meer aanhangen later in de oefening
        return map
    
def find_antinode_positions(coordinates1, coordinates2):
    x1, y1 = coordinates1
    x2, y2 = coordinates2
    return Coordinates(x1 - (x2-x1), y1 - (y2-y1)), Coordinates(x2 + (x2-x1), y2 + (y2-y1))

def find_antinodes_position_partB(map, coordinates1, coordinates2):
    row1, column1 = coordinates1
    row2, column2 = coordinates2
    
    antinode_position_list = []
    
    row_delta = row2 - row1
    column_delta = column2 - column1
    
    row_delta_min = row_delta / math.gcd(abs(row_delta), abs(column_delta))
    column_delta_min = column_delta / math.gcd(abs(row_delta), abs(column_delta))
    
    next_antinode_dir1 = int(row1), int(column1)
    next_antinode_dir2 = int(row1 + row_delta_min), int(column1 + column_delta_min)
    
    while (ArrayHelper.is_in_array_bounds(map, next_antinode_dir1[0], next_antinode_dir1[1])):
        antinode_position_list.append(next_antinode_dir1)
        next_antinode_dir1 = int(next_antinode_dir1[0] - row_delta_min), int(next_antinode_dir1[1] - column_delta_min)
    
    while (ArrayHelper.is_in_array_bounds(map, next_antinode_dir2[0], next_antinode_dir2[1])):
        antinode_position_list.append(next_antinode_dir2)
        next_antinode_dir2 = int(next_antinode_dir2[0] + row_delta_min), int(next_antinode_dir2[1] + column_delta_min)
        
    return(antinode_position_list)

def is_antenna(value):
    return value[0].islower() or value[0].isupper() or value[0].isdigit()
    
    
def mark_antinodes(map):
    
    rowcount, columncount = map.shape
    map_with_antinodes = copy.deepcopy(map)
    
    for r in range(rowcount):
        for c in range(columncount):
            if (is_antenna(map[r][c])):
                r_next, c_next = ArrayHelper.find_next_coordinates_that_contain(map, map[r][c][0], start_index= ArrayHelper.find_next_coordinate(map, r, c))
                
                while (r_next != -1):
                    pos1, pos2 = find_antinode_positions(Coordinates(r,c),Coordinates(r_next, c_next))
                
                    if (ArrayHelper.is_in_array_bounds(map, pos1.row, pos1.column)):
                        if "#" not in map_with_antinodes[pos1.row][pos1.column]:
                            map_with_antinodes[pos1.row][pos1.column] += "#" 
                    if (ArrayHelper.is_in_array_bounds(map, pos2.row, pos2.column)):
                        if "#" not in map_with_antinodes[pos2.row][pos2.column]:
                            map_with_antinodes[pos2.row][pos2.column] += "#"                        
                    r_next, c_next = ArrayHelper.find_next_coordinates_that_contain(map, map[r][c][0], start_index=ArrayHelper.find_next_coordinate(map, r_next, c_next))
                    
    return map_with_antinodes

def mark_antinodes_partB(map):
    
    rowcount, columncount = map.shape
    map_with_antinodes = copy.deepcopy(map)
    
    for r in range(rowcount):
        for c in range(columncount):
            if (is_antenna(map[r][c])):
                r_next, c_next = ArrayHelper.find_next_coordinates_that_contain(map, map[r][c][0], start_index= ArrayHelper.find_next_coordinate(map, r, c))
                
                while (r_next != -1): 
                    antinodes = find_antinodes_position_partB(map, Coordinates(r,c),Coordinates(r_next, c_next))
                    
                    for antinode in antinodes:
                        if "#" not in map_with_antinodes[antinode[0]][antinode[1]]:
                            map_with_antinodes[antinode[0]][antinode[1]] += "#" 
                    r_next, c_next = ArrayHelper.find_next_coordinates_that_contain(map, map[r][c][0], start_index=ArrayHelper.find_next_coordinate(map, r_next, c_next))

                                        
    return map_with_antinodes
                        
def count_antinodes(map):
    counter = 0
    rowcount, columncount = map.shape
    
    for r in range(rowcount):
        for c in range(columncount):
            if ("#" in map[r][c]):
                counter += 1
                
    return counter

                        


print("=================== part A ===================")
with ExecutionTimer():
    antenna_map = transform_input(INPUT)
    antenna_and_antinode_map = mark_antinodes(antenna_map)
    print(count_antinodes(antenna_and_antinode_map))
    
# 369
# Execution time: 0 hours, 0 minutes, 0 seconds, 68.6232 milliseconds

    

    
print("=================== part B ===================")
with ExecutionTimer():
    antenna_map = transform_input(INPUT)
    antenna_and_antinode_map = mark_antinodes_partB(antenna_map)
    print(count_antinodes(antenna_and_antinode_map))
    
# 1169
# Execution time: 0 hours, 0 minutes, 0 seconds, 62.5935 milliseconds


# Veel gefoefeld, ook geen mooie code. 
# Geleerd, bij het omvormen naar een array van strings, moeten we specifiek voorzien dat we 2 karakters aankunnen. Want bij strings neemt numpy het niet ruim 




    






