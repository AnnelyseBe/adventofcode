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
TEST_INPUT_A = BASE_DIR / 'input_test_A'

Token_combination = namedtuple('Token_combination', ['A', 'B', 'token_count'])
Robot = namedtuple('Robot', ['rank', 'x','y','dx','dy'])
Robot_loc = namedtuple('Robot_loc', ['rank', 'x','y'])
EVALUTION_TIME = 100


def transform_input(inputlocation):
    with open(inputlocation) as file:
        all_robot_details = re.findall('p=(\d+),(\d+) v=(.*\d+),(.*\d+)', file.read())
        robots = []
        for index, robot_details in enumerate(all_robot_details):
            robots.append(Robot(index, *map(int, robot_details)))
        return robots
    
def calculate_location(robot, time, tiles_horizontal, tiles_vertical):
    x = (robot.x + time * robot.dx) % tiles_horizontal
    y = (robot.y + time * robot.dy) % tiles_vertical
    return robot.rank, x, y

def write_room_in_file(room, time):
    file = BASE_DIR / 'robots_in_time'
    row_count, column_count = room.shape
    
    with open(file, "a") as myfile:
        myfile.write(f'Room at {time} sec =============================================================================================')
        myfile.write('\n')
    
        for row in range(row_count):
            for column in range(column_count):
                myfile.write(room[row][column])
            myfile.write('\n')
                
            
        
    




print("=================== part A ===================")
with ExecutionTimer():
    input = INPUT
    robots = transform_input(input)
    room_x, room_y = 101, 103
    
    if (input == TEST_INPUT_A):
        room_x, room_y = 11, 7
        
    quadrants = {}
    safety_factor = 1
        
    for robot in robots:
        rank, x, y = calculate_location(robot, EVALUTION_TIME, room_x, room_y)
        
        if (y < room_y//2):
            if (x < room_x//2):
                quadrants[1] = quadrants.get(1, 0) + 1
            elif (room_x//2 < x < room_x):
                quadrants[2] = quadrants.get(2, 0) + 1
        elif (room_y//2 < y < room_y):
            if (x < room_x//2):
                quadrants[3] = quadrants.get(3, 0) + 1
            elif (room_x//2 < x < room_x):
                quadrants[4] = quadrants.get(4, 0) + 1
                    
    for robot_count in quadrants.values():
        safety_factor *= robot_count
        
    print(f"{safety_factor}")   
# 229868730
# Execution time: 0 hours, 0 minutes, 0 seconds, 7.2862 milliseconds

        
    
print("=================== part B ===================")
with ExecutionTimer():
    input = INPUT
    robots = transform_input(input)
    room_x, room_y = 101, 103
    
    if (input == TEST_INPUT_A):
        room_x, room_y = 11, 7
        
    
    
    for time in range(1,10000):
        room = np.full((room_y, room_x), ' ')
        for robot in robots:
            rank, x, y = calculate_location(robot, time, room_x, room_y)
            room[y,x] = 'X'
        write_room_in_file(room, time)
# Execution time: 0 hours, 1 minutes, 59 seconds, 356.3763 milliseconds
# Alles naar een file laten schrijven en dan zoeken op de langste opeenvolging van XXXXXXX-en -> blijkbaar op 7861 sec
    

    












