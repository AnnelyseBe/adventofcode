from utils.execution_timer import ExecutionTimer
from collections import namedtuple, Counter
import numpy as np
from pathlib import Path
import re


# Define the base directory relative to the current script's location
BASE_DIR = Path(__file__).parent  # Path to the current script's folder

# Define paths to your input files dynamically
INPUT = BASE_DIR / 'input'
TEST_INPUT = BASE_DIR / 'input_test'
TEST_INPUT_B = BASE_DIR / 'input_test_B'

rules = []
updates = []
incorrect_updates = []


def transform_input(inputlocation):
    with open(inputlocation) as file:
        parts = file.read().split('\n\n')
        rule_part = parts[0].splitlines()        
        rules = [(int(re.findall(r'\d+', line)[0]), int(re.findall(r'\d+', line)[1])) for line in rule_part]
        updates = [list(map(int,line.split(','))) for line in parts[1].splitlines()]
        return rules, updates
    
def validate_update_pages(update, rules):
    correct_order = True
    for index, page in enumerate(update):
        for rule in rules: 
            if rule[0] == page:
                if (rule[1] in update[:index]):
                    return False
    return correct_order

def fix_updates_pages(update, rules):
    fixed_update = []
    for index, page in enumerate(update):
        lowest_new_index = index
        for rule in rules: 
            if (rule[0] == page and rule[1] in update[:index]):
                lowest_new_index = min(lowest_new_index, update.index(rule[1]))
        fixed_update.insert(lowest_new_index, page)
                            
    return fixed_update, fixed_update[len(fixed_update)//2]
    

print("=================== part A ===================")
with ExecutionTimer():
    rules, updates = transform_input(INPUT)
    counter = 0
    for update in updates:
        if(validate_update_pages(update, rules)):
            counter += update[len(update)//2]
        else: 
            incorrect_updates.append(update)
            
    print(counter)

# 7074
# Execution time: 0 hours, 0 minutes, 0 seconds, 105.2358 milliseconds
            
    
print("=================== part B ===================")
with ExecutionTimer():
    
    counter = 0
    
    is_correct = False
    iteration = 1
        
    while(not is_correct):
        
        temp_fix = []
        counter = 0
    
        for update in incorrect_updates:
            fixed_or_not , middle = fix_updates_pages(update,rules)
            temp_fix.append(fixed_or_not)
            counter += middle
            
        is_correct = all(validate_update_pages(update, rules) for update in temp_fix)
        iteration += iteration
        incorrect_updates = temp_fix
        
    print(counter)

# 4828
# Execution time: 0 hours, 0 minutes, 0 seconds, 530.6508 milliseconds
    
        
        


    












