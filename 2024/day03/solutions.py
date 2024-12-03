from utils.execution_timer import ExecutionTimer
from collections import namedtuple, Counter
import re
import numpy as np

INPUT = './2024/day03/input'
TEST_INPUT = './2024/day03/input_test'
TEST_INPUT_B = './2024/day03/input_test_B'

def transform_input(inputlocation):
    with open(inputlocation) as file:
        string_for_extraction = file.read()
        return string_for_extraction
    
def extract_multiplications(multiplication_string):
    # Find all "mul(x,y)" patterns and extract the numbers x and y as tuples -> omdat (\d+) tussen haakjes staan, weten we dat we enkel dat van de regex gaan bijhouden 
    multiplications = re.findall(r'mul\((\d+),(\d+)\)', multiplication_string)
        
    left_multiplication = np.array([int(x) for x, _ in multiplications])
    right_multiplication = np.array([int(y) for _, y in multiplications])
    return left_multiplication, right_multiplication

def transform_input_B(inputlocation):
    with open(inputlocation) as file:
        content = file.read()
                
        # Split the content based on 'do()' or 'don't()' -> alles we tussen haakjes zetten dat houden we ook bij
        input_parts = re.split(r"(do\(\)|don't\(\))", content)
        strings_for_extraction = []
        
        for index in range(0,len(input_parts),2):
            if (index == 0):
                strings_for_extraction.append(input_parts[index])
            elif (input_parts[index-1] == f'do()'):
                strings_for_extraction.append(input_parts[index])
                
        return strings_for_extraction

    


print("=================== part A ===================")
with ExecutionTimer():
    multiplication_string = transform_input(INPUT)
    left_multiplication, right_multiplication = extract_multiplications(multiplication_string)
    results = left_multiplication * right_multiplication
    sum_results = sum(results)
    
    print(sum_results)

    
print("=================== part B ===================")
with ExecutionTimer():
    multiplication_strings = transform_input_B(INPUT)
    
    left_multiplication = []
    right_multiplication= []
    
    for ms in multiplication_strings:
        left_part, right_part = extract_multiplications(ms)
        left_multiplication = np.hstack((left_multiplication, left_part)) # 1D arrays moet je horizontaal stacken (en in een tuple precies ????)
        right_multiplication = np.hstack((right_multiplication, right_part))
    
    results = left_multiplication * right_multiplication
    sum_results = sum(results)
    
    print(sum_results)

    












