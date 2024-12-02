from utils.execution_timer import ExecutionTimer
from collections import namedtuple, Counter
import re

INPUT = './2023/day08/input'
TEST_INPUT = './2023/day08/input_test'

directions = []
nodes = {}




def transform_input(inputlocation):
    with open(inputlocation) as file:
        lines = file.read().splitlines()
        
        directions.extend([letter for letter in lines[0]])
        
        for line in lines[2:]:
            points = re.findall(r'[a-zA-Z]+',line)
            node_origin = points[0]
            node_left = points[1]
            node_right = points[2]
            nodes[node_origin] = (node_left, node_right)
            
def find_next_node(start_node, direction):
    next_node = nodes[start_node][0] if direction == 'L' else nodes[start_node][1]
    return next_node
    



print("=================== part A ===================")
with ExecutionTimer():
    transform_input(TEST_INPUT)
    
    while (next_node != 'ZZZ')
        blablabla
    
    
    
    

    
print("=================== part B ===================")
# with ExecutionTimer():











