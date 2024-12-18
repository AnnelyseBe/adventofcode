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
TEST_INPUT_B = BASE_DIR / 'input_test_B'
TEST_INPUT_C = BASE_DIR / 'input_test_C'

Claw_machine = namedtuple('Claw_machine', ['a_x', 'a_y', 'b_x', 'b_y', 'p_x', 'p_y'])
Token_combination = namedtuple('Token_combination', ['A', 'B', 'token_count'])
TOKEN_A = 3
TOKEN_B = 1

def transform_input(inputlocation):
    with open(inputlocation) as file:
        all_machines = re.findall('Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)',file.read())
        result = []
        for machine in all_machines:
            result.append(Claw_machine(*map(int, machine)))
        return result
    
def transform_input_partB(claw_machines):
    claw_machines_transformed = []
    
    for machine in claw_machines:
        claw_machines_transformed.append(Claw_machine(machine[0], machine[1], machine[2], machine[3], machine[4] + 10000000000000, machine[5] + 10000000000000))
        
    return claw_machines_transformed
        
def A_B_combinations_for_position(a_x, b_x, p_x, max_presses):
    combinations = []
    
    for A in range (0,max_presses):
        if (A * a_x > p_x):
            break
        for B in range (0,max_presses):
            if (A * a_x + B * b_x > p_x):
                break
            elif (A * a_x + B * b_x == p_x):
                combinations.append(Token_combination(A, B, A * TOKEN_A + B * TOKEN_B ))
                
    def sort_by_tokens(combination):
        return combination.token_count
    
    combinations.sort(key=sort_by_tokens)
    return combinations

def find_best_combination_with_matrices(machine):
    M = np.array([[machine.a_x, machine.b_x], [machine.a_y, machine.b_y]]) # coëfficiëntenmatrix
    p = np.array([machine.p_x, machine.p_y]) # vector met de bekende waarden
    
    # Bereken de inverse en los op
    try:
        x = np.linalg.inv(M).dot(p)
        A, B = x
        A = round(A, 3) # round om de afrondingsissues weg te werken
        B = round(B, 3)
        if (A.is_integer() and B.is_integer()): # we willen enkel de gehele oplossingen 
            combination = Token_combination(A, B, A * TOKEN_A + B * TOKEN_B )
            return combination
        
    except np.linalg.LinAlgError:
        return -1
        
    return -1

print("=================== part A ===================")
with ExecutionTimer():
    claw_machines = transform_input(INPUT)
    sum_tokens = 0
    combinations_for_x_and_y = []
    
    for machine in claw_machines:
        combinations_for_x = A_B_combinations_for_position(machine.a_x, machine.b_x, machine.p_x, 100)

        for combination in combinations_for_x:
            if (combination.A * machine.a_y + combination.B * machine.b_y == machine.p_y):
                sum_tokens += combination.token_count
                break
            
    print(sum_tokens)
        
# 29517
# Execution time: 0 hours, 0 minutes, 0 seconds, 480.2396 milliseconds
# Eigenlijk had dit al met matrices gemoeten. Soms is logisch nadenken ipv beginnen itereren wel interessant -> als we het oplossen op de manier van part B (zonder de transform_input_partB) dan kan het op 7,6 milliseconds

        
print("=================== part B ===================") # zoals het moet, met matrices
with ExecutionTimer():
    sum_tokens = 0
    claw_machines = transform_input(INPUT)
    # claw_machines = transform_input_partB(claw_machines)    
      
    for machine in claw_machines:
        combination = find_best_combination_with_matrices(machine)
        
        if (combination != -1):
            sum_tokens += combination.token_count
            
    print(sum_tokens)
    
# 103570327981381.0
# Execution time: 0 hours, 0 minutes, 0 seconds, 14.2652 milliseconds
# Lastige zaak aan de matrices zijn de afrondingsissues met de floats. Hierdoor moeten we een round() inbouwen, zodat de floats terug naar de corresponderende int worden omgezet
# Een optie om NumPy’s np.linalg.solve te gebruiken in plaats van np.linalg.inv kan de prestaties verder verbeteren (suggestie van chatGPT)
            

    












