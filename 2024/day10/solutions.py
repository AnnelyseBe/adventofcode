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
TEST_INPUT_B = BASE_DIR / 'input_test_B'

directions = [(0,1), (1,0), (0,-1), (-1,0)]
richting = ["rechts", "onder", "links", "boven"]

def transform_input(inputlocation):
    with open(inputlocation) as file:
        grid = np.array([list(map(int, line)) for line in file.read().splitlines()])
        trailheads = np.where(grid == 0) # geeft tuple van 2 1-D array's. Eerste array met rij-index, tweede array met kolom-index
        trailheads = list(zip(trailheads[0], trailheads[1]))
        return grid, trailheads
    
def find_paths_endpoints(startpoint, height, grid):
    rowcount, columncount = grid.shape
    x, y = startpoint
    paths = 0
    endpoints = []
    
    for i in range(len(directions)):
        dx, dy = directions[i]
        if (0 <= x+dx < rowcount and 0 <= y+dy < columncount):
            if (grid[x+dx,y+dy]) == height + 1: # VALID POINT
                if height + 1 == 9: # END
                    endpoints.extend([(x+dx, y+dy)])
                    paths += 1
                else:
                    paths_next, endpoints_next = find_paths_endpoints((x+dx, y+dy), height + 1, grid)
                    paths += paths_next
                    endpoints.extend(endpoints_next)
                    
    return paths, endpoints
            
print("=================== part A, B ===================")
with ExecutionTimer():
    grid, trailheads = transform_input(INPUT)
    total_paths = 0
    sum_endpoints = 0
    
    paths, endpoints = find_paths_endpoints((0,2), 0, grid)

    for i in range(len(trailheads)):
        paths_trail, endpoints_trail = find_paths_endpoints(trailheads[i],0, grid)
        total_paths += paths_trail
        sum_endpoints += len(set(endpoints_trail))
        
    print(f"part A: {sum_endpoints}")
    print(f"part B: {total_paths}")

    
# recursive gewerkt, blijft voor mij toch een beetje een mindfuck.
# begonnen van een andere deelnemer aan advent of code. Dit was de eerste keer dat ik echt code gepikt heb (geen probleem, veel uit geleerd).
# ik heb echter nog wel veel moeten zoeken, want ik had de opgave wat fout gelezen en degene van wie ik de oplossing pikte, die precies ook

