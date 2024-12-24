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
TEST_INPUT_A = BASE_DIR / 'input_test'
TEST_INPUT_B = BASE_DIR / 'input_test_B'
TEST_INPUT_C = BASE_DIR / 'input_test_C'


def transform_input(inputlocation):
    with open(inputlocation) as file:
        return np.array([[char for char in line] for line in file.read().splitlines()])
    
def get_neighbourcount(garden, row, column):
    neighbour_count = 0
    
    neighbour_north = ArrayHelper.valid_neighbour_coordinates_and_value(garden, "NORTH", (row, column))
    neighbour_south = ArrayHelper.valid_neighbour_coordinates_and_value(garden, "SOUTH", (row, column))
    neighbour_east = ArrayHelper.valid_neighbour_coordinates_and_value(garden, "EAST", (row, column))
    neighbour_west = ArrayHelper.valid_neighbour_coordinates_and_value(garden, "WEST", (row, column))
    
    if (neighbour_north[1] != None and neighbour_north[1] == garden[row][column]):
        neighbour_count += 1
    if (neighbour_south[1] != None and neighbour_south[1] == garden[row][column]):
        neighbour_count += 1
    if (neighbour_east[1] != None and neighbour_east[1] == garden[row][column]):
        neighbour_count += 1
    if (neighbour_west[1] != None and neighbour_west[1] == garden[row][column]):
        neighbour_count += 1
    return neighbour_count
    
def get_region(garden, row, column, visited=None): # met behulp van chatgpt
    if visited is None:
        visited = set()  # Initialize the visited set on the first call
    
    directions = ["EAST", "WEST", "NORTH", "SOUTH"]
    points_in_area = {}

    region = garden[row][column]

    if (row, column) in visited:
        return points_in_area  # Skip if already visited

    # Mark the current point as visited
    visited.add((row, column))
    points_in_area[(row, column)] = get_neighbourcount(garden, row, column)

    # Explore neighbors
    for direction in directions:
        neighbour = ArrayHelper.valid_neighbour_coordinates_and_value(garden, direction, (row, column))
        if neighbour[0] and neighbour[1]:
            (neighbour_row, neighbour_column), neighbour_value = neighbour
            if (neighbour_value == region) and ((neighbour_row, neighbour_column) not in visited):
                points_in_area.update(get_region(garden, neighbour_row, neighbour_column, visited))

    return points_in_area
    

print("=================== part A ===================")
with ExecutionTimer():
    garden = transform_input(INPUT)
    print(garden)
    rowcount, columncount = garden.shape
    cost = 0
    
    for row in range(rowcount):
        for column in range(columncount):
            if (garden[row][column].isalpha()):
                print(f"{garden[row][column]} is een letter")
                points_in_area = get_region(garden, row, column)
                area = 0
                fence = 0
                for coordinates, neighbours in points_in_area.items():
                    x, y = coordinates
                    area += 1
                    fence += 4-neighbours
                    garden[x][y] = '.'
                print(f"cost {area * fence}; area {area}; fence {fence}")
                cost += (area * fence)
    print(cost)

# 1363484
# Execution time: 0 hours, 0 minutes, 0 seconds, 474.6124 milliseconds (met print comments)
                
                    

    

    
print("=================== part B ===================")
with ExecutionTimer():
    print("todo")
    
    
    # recursive, krijg ik een punthoofd van. Chatgpt hielp me met die visited, maar ik zou er zelf niet op gekomen zijn. Ik vraag me of of dit ook via een while loop kan
                
                

    












