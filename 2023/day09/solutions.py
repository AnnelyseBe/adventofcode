from utils.execution_timer import ExecutionTimer
from collections import namedtuple, Counter
import numpy as np

INPUT = './2023/day09/input'
TEST_INPUT = './2023/day09/input_test'
TEST_INPUT_B = './2023/day09/input_test_B'

def transform_input(inputlocation):
    with open(inputlocation) as file:
        content = file.read().splitlines()
        histories = [[int(number) for number in history.split()] for history in content]
        print(histories)
        return histories
        
def prediction_next_value(history):
    extrapolation_lines = []
    extrapolation_lines.append(history)
        
    while(not all(number == 0 for number in extrapolation_lines[-1])):
        diff_line = np.diff(np.array(extrapolation_lines[-1])) 
        print(f'list(diff_line): {list(diff_line)}')
        extrapolation_lines.append(list(diff_line))
        
        print(extrapolation_lines)




print("=================== part A ===================")
with ExecutionTimer():
    histories = transform_input(TEST_INPUT)
    for history in histories:
        print(f'History ============================== {history}={type(history)}')
        prediction_next_value(history)
    # next_values = [prediction_next_value(history) for history in histories]

    

    
print("=================== part B ===================")
with ExecutionTimer():
    print("todo")

    












