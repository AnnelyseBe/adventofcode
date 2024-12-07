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
        content = file.read().splitlines()
        test_values = [int(line.split(':')[0]) for line in content]
        equations = [list(map(int,line.split(':')[1].split())) for line in content]
        return test_values, equations

def get_all_combinations(operators, length): # todo, hier zou memoization wel interessant zijn
    return list(product(operators, repeat=length)) # carthesiaans product

def is_equation_solvable(equation, test_value, operators):
    combinations = get_all_combinations(operators, len(equation)-1)
    
    for combination in combinations:
        result = equation[0]
        for i in range(len(equation)-1):
            if (combination[i] == '+'):
                result += equation[i+1]
            elif (combination[i] == '*'):
                result *= equation[i+1]
            elif (combination[i] == '|'):
                result = int(str(result) + str(equation[i+1]))
        if (test_value == result):
            return True
        
    return False
            
    
    
    



print("=================== part A ===================")
with ExecutionTimer():
    test_values, equations = transform_input(INPUT)
    operators = '+*'
    
    possible_testvalues_sum = 0
    
    for i, equation in enumerate(equations):
        if (is_equation_solvable(equation, test_values[i], operators)):
            possible_testvalues_sum += test_values[i]
    
    print(possible_testvalues_sum)
    
# 42283209483350
# Execution time: 0 hours, 0 minutes, 0 seconds, 216.8575 milliseconds

    

    
print("=================== part B ===================")
with ExecutionTimer():
    test_values, equations = transform_input(INPUT)
    operators = '+*|'
    
    possible_testvalues_sum = 0
    
    for i, equation in enumerate(equations):
        if (is_equation_solvable(equation, test_values[i], operators)):
            possible_testvalues_sum += test_values[i]
    
    print(possible_testvalues_sum)
    
# 1026766857276279
# Execution time: 0 hours, 0 minutes, 15 seconds, 325.0657 milliseconds

# ongeveer 45 min aan gewerkt (opgave al op voorhand gelezen)