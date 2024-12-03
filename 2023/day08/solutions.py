from utils.execution_timer import ExecutionTimer
from collections import namedtuple, Counter
import re
from math import lcm

INPUT = './2023/day08/input'
TEST_INPUT = './2023/day08/input_test'
TEST_INPUT_2 = './2023/day08/input_test_2'


def transform_input(inputlocation):
    with open(inputlocation) as file:
        lines = file.read().splitlines()
        
        directions = []        
        directions.extend([letter for letter in lines[0]])
        nodes = {}
        
        
        for line in lines[2:]:
            points = re.findall(r'[0-9a-zA-Z]+',line)
            node_origin = points[0]
            node_left = points[1]
            node_right = points[2]
            nodes[node_origin] = (node_left, node_right)
            
        return directions, nodes
            
def find_next_node(start_node, direction):
    next_node = nodes[start_node][0] if direction == 'L' else nodes[start_node][1]
    return next_node
    



print("=================== part A ===================")
with ExecutionTimer():
    directions, nodes = transform_input(INPUT)
    
    next_node = 'AAA'
    step = 0
    
    while (next_node != 'ZZZ'):
        next_node = find_next_node(next_node, directions[step%len(directions)])
        step += 1
        
    print(step)

# 11567
# Execution time: 0 hours, 0 minutes, 0 seconds, 8.9996 milliseconds
       
print("=================== part B ===================")
with ExecutionTimer():
    directions, nodes = transform_input(INPUT)
    # print(nodes)
    
    next_nodes = [key for key in nodes if key.endswith('A')]
    # print(next_nodes)

    step = 0
    
    while (not all(node.endswith('Z') for node in next_nodes)):
        temp = []
        # print(step)
        for node in next_nodes:
            next_node = find_next_node(node, directions[step%len(directions)])
            temp.append(next_node)
        # print(temp)
            
        next_nodes.clear()
        next_nodes.extend(temp)
        # print(next_nodes)
        step += 1
        
    print(step)
 
print("=================== part B =================== smarter ===================")   
with ExecutionTimer():
    directions, nodes = transform_input(INPUT)
    
    starting_nodes = [key for key in nodes if key.endswith('A')]
    step_counts = {}
    
    for start_node in starting_nodes:
        next_node = start_node
        step = 0
    
        while (not next_node.endswith('Z')):
            next_node = find_next_node(next_node, directions[step%len(directions)])
            step += 1
        step_counts[start_node] = step
        
    print(step_counts)
    print(lcm(*step_counts.values()))
    
# 9858474970153
# Execution time: 0 hours, 0 minutes, 0 seconds, 63.7431 milliseconds
    
# de truk is niet om het in parallel te doen, maar afzonderlijk 1 loep van elk level dat eindigt op A. Dan berekenen we het aantal steps. 
# En nadien kunnen we het LCM, lowest common multiplier bepalen. 
# hier op de laatste regel zien we ook het nut van unpacken











