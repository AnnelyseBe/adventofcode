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

def transform_input(inputlocation):
    with open(inputlocation) as file:
        return file.read()

def show_disk_layout(disk_map):
    disk_layout = []
    
    for index, digit in enumerate(disk_map):
        partition_layout = []
        
        if (index % 2 == 0):
            id = int(index / 2)
            for place in range(int(digit)):
                partition_layout.append(id)
        else:
            for place in range(int(digit)):
                partition_layout.append('.')
                
        disk_layout.extend(partition_layout)
    return disk_layout

def find_index_last_digit(disk_layout):
    # Find the index of the last digit, next function returns first value where statement is True
    last_digit_index = next((i for i in reversed(range(len(disk_layout))) if isinstance(disk_layout[i], int)), None)
    return last_digit_index

def find_index_first_point(disk_layout):
    index_first_point = next((i for i in range(len(disk_layout)) if disk_layout[i]== '.'), None)
    return index_first_point

def find_index_first_x(disk_layout, to_search, repetitioncount):
    
    i = 0
    while (i < len(disk_layout)):
        still_ok = True
        for j in range(repetitioncount):
            if (i+j >= len(disk_layout) or disk_layout[i+j] != to_search):
                still_ok = False
                break
        if (still_ok): # position found
            return i
        else:
            i = i + j + 1 
            
    return -1

def find_index_first(disk_layout, to_search):
    index_first = next((i for i in range(len(disk_layout)) if disk_layout[i]== to_search), None)
    return index_first

def find_index_last(disk_layout, to_search):
    # Find the index of the last digit, next function returns first value where statement is True
    index_last = next((i for i in reversed(range(len(disk_layout))) if disk_layout[i]== to_search), None)
    return index_last

def is_completely_compressed(disk_layout):
    index_last_digit = find_index_last_digit(disk_layout)
    return '.' not in disk_layout[:index_last_digit]
    
def compact_disk_layout(disk_layout):
    while (not is_completely_compressed(disk_layout)):
        index_last_digit = find_index_last_digit(disk_layout)
        last_digit = disk_layout[index_last_digit]
        index_first_point = find_index_first_point(disk_layout)
        
        
        disk_layout[index_last_digit] = '.'
        disk_layout[index_first_point] = last_digit  
        
def compact_disk_layout_with_framentation(disk_layout):
    
    disk_compacted_fragmented = disk_layout.copy()
    # print(disk_compacted_fragmented)
    index = -1 
    # print(f"max_file_id: {disk_layout[index]}")

    begin_index_file_id = find_index_first(disk_layout, disk_layout[index])
    eind_index_file_id = find_index_last(disk_layout, disk_layout[index])
    
    while(index is not None):
    
        length_file_id = eind_index_file_id - begin_index_file_id + 1
        # print(f"max_file_id: {disk_layout[index]}, begin_index_file_id: {begin_index_file_id}, eind_index_file_id: {eind_index_file_id}, length_file_id: {length_file_id}")
        free_index = find_index_first_x(disk_compacted_fragmented[:index], '.', length_file_id)
        # print(f"free index: {free_index}")
    
        if (free_index != -1):
            for i in range(length_file_id):
                disk_compacted_fragmented[begin_index_file_id + i] = '.'
                disk_compacted_fragmented[free_index + i] = disk_layout[index]
                
        old_begin_index = begin_index_file_id
            
        index = find_index_last_digit(disk_layout[0:begin_index_file_id])  
        if (index is None):
            break
        begin_index_file_id = find_index_first(disk_layout[0:old_begin_index], disk_layout[index])
        eind_index_file_id = find_index_last(disk_layout[0:old_begin_index], disk_layout[index])
        # print(f"max_file_id: {disk_layout[index]}, begin_index_file_id: {begin_index_file_id}, eind_index_file_id: {eind_index_file_id}, length_file_id: {length_file_id}")
        # print(disk_compacted_fragmented)
        
    return disk_compacted_fragmented

print("=================== part A ===================")
with ExecutionTimer():
    disk_map = transform_input(INPUT)
    disk_layout = show_disk_layout(disk_map)
    compact_disk_layout(disk_layout)
    
    index_last_digit = find_index_last_digit(disk_layout)
    
    checksum = 0
    for index, number in enumerate(disk_layout[:index_last_digit + 1]):
        checksum += index * number
        
    print(checksum)
    
# 6334655979668
# Execution time: 0 hours, 1 minutes, 27 seconds, 528.3344 milliseconds

print("=================== part B ===================")
with ExecutionTimer():
    disk_map = transform_input(INPUT)
    disk_layout = show_disk_layout(disk_map)
    disk_compacted_fragmented = compact_disk_layout_with_framentation(disk_layout)
    
    index_last_digit = find_index_last_digit(disk_layout)
    
    checksum = 0
    for index, number in enumerate(disk_compacted_fragmented[:index_last_digit + 1]):
        if (number != '.'):
            checksum += index * number
            
    print(checksum)
    
# 6349492251099
# Execution time: 0 hours, 1 minutes, 30 seconds, 21.6408 milliseconds
    
    
# vreselijke code, slechte naamgeving. Methodes die zouden kunnen gerefactored en gecombineerd worden, memoization die zou kunnen worden toegepast
# het gaat ook niet bijzonder snel
# maar het werkt wel           
