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


def transform_input(inputlocation):
    with open(inputlocation) as file:
        return [int(stone) for stone in file.read().split()]
    
def blink_one_stone(stone):
    stones_after_blink = []
    if (stone == 0):
        stones_after_blink.append(1)
    elif (len(str(stone)) % 2 == 0):
        stones_after_blink.append(int(str(stone)[0:(len(str(stone))//2)]))
        stones_after_blink.append(int(str(stone)[len(str(stone))//2:]))
    else:
        stones_after_blink.append(stone*2024)
    return stones_after_blink
    
    
def blink(stones):
    stones_after_blink = []
    for stone in stones:
        stones_after_blink.extend(blink_one_stone(stone))

    return stones_after_blink

def blink_and_think(stones_count):
   
    stones_count_after_blink = {}
    for stone, occurence_count in stones_count.items():
        result = blink_one_stone(stone)
        
        for stone_for_result in result:
            stones_count_after_blink[stone_for_result] = stones_count_after_blink.get(stone_for_result,0) + occurence_count
        
    return stones_count_after_blink

print("=================== part A ===================")
with ExecutionTimer():
    stones = transform_input(INPUT)
    blinks = 25
    print(stones)
    
    for i in range(blinks):
        stones = blink(stones)
    print(len(stones))
    
# 191690
# Execution time: 0 hours, 0 minutes, 0 seconds, 331.3959 milliseconds
    

    
print("=================== part B ===================")
with ExecutionTimer():
    stones = transform_input(INPUT)
    blinks = 75
    stone_sum = 0
    

    stones_count = {}
    # fill stones count with stone value and occurance
    for stone in stones:
        stones_count[stone] = stones_count.get(stone, 0) + 1
        
    for i in range(blinks):
        stones_count = blink_and_think(stones_count)
        
    for stone_occurence in stones_count.values():
        stone_sum = stone_sum + stone_occurence
        
    print(stone_sum)
    
# 228651922369703
# Execution time: 0 hours, 0 minutes, 0 seconds, 119.3020 milliseconds

# Het probleem is dat na die interaties, het max aantal voor een lijst overschreden wordt. Beter een dict gebruiken die voor elke waarde van de steen bijhoudt hoeveel deze voorkomt. De volgorde van de stenen is immers niet belangrijk
        

    












