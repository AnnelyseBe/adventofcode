from utils.execution_timer import ExecutionTimer
from utils.array_helper import ArrayHelper
from collections import namedtuple, Counter
import numpy as np
from pathlib import Path
import re
from itertools import product 


# Define the base directory relative to the current script's location
BASE_DIR = Path(__file__).parent  # Path to the current script's folder

# Define paths to your input files dynamically
INPUT = BASE_DIR / 'input'
TEST_INPUT = BASE_DIR / 'input_test'
TEST_INPUT_B = BASE_DIR / 'input_test_B'


def transform_input(inputlocation):
    with open(inputlocation) as file:
        print("todo")




print("=================== part A ===================")
with ExecutionTimer():
    transform_input(TEST_INPUT)
    print("todo")

    

    
print("=================== part B ===================")
with ExecutionTimer():
    transform_input(TEST_INPUT)
    print("todo")

    












