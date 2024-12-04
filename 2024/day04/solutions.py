from utils.execution_timer import ExecutionTimer
from collections import namedtuple, Counter
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent  # Path to the current script's folder
INPUT = BASE_DIR / 'input'
TEST_INPUT = BASE_DIR / 'input_test'
TEST_INPUT_B = BASE_DIR / 'input_test_B'

def transform_input(inputlocation):
    with open(inputlocation) as file:
        content = [list(line) for line in file.read().splitlines()]
        puzzle = np.array(content)
        return puzzle
    
def find_pattern(puzzle, pattern):
    count_horizontal = find_horizontal(puzzle, pattern)
    count_vertical = find_horizontal(puzzle.T, pattern) # array transposed
    count_diagonal = find_diagonal(puzzle, pattern)
    count_diagonal2 = find_diagonal(np.fliplr(puzzle), pattern) # array flipped
    return count_horizontal + count_vertical + count_diagonal + count_diagonal2

def find_pattern_XMAS(puzzle):
    count = 0
    rowcount, columncount = puzzle.shape
    
    for row in range(rowcount - 2): # 2 laatste rijen kunnen niet het begin van het patroon zijn
        for column in range(columncount - 2): # 2 laatste kolommen kunnen niet het begin van het patroon zijn           
            if (puzzle[row+1][column+1] == 'A' 
                and
                (puzzle[row][column] == 'M' and puzzle[row+2][column+2] == 'S'
                or 
                puzzle[row][column] == 'S' and puzzle[row+2][column+2] == 'M')
                and 
                (puzzle[row][column+2] == 'M' and puzzle[row+2][column] == 'S'
                or 
                puzzle[row][column+2] == 'S' and puzzle[row+2][column] == 'M')):
                count += 1
    return count
                
def find_horizontal(puzzle, pattern):    
    count = 0
    pattern_rev= pattern[::-1]
    l = len(pattern)
    
    for row in puzzle:
        for i in range(len(row)-(len(pattern)+1)):
            if (''.join(row[i:i+l]) == pattern or ''.join(row[i:i+l]) == pattern_rev):
                count +=1
    return count

def find_diagonal(puzzle, pattern):    
    count = 0
    pattern_rev= pattern[::-1]
    l = len(pattern)
    
    for o in range(-len(puzzle)+1,len(puzzle[0])):
        diagonal = puzzle.diagonal(offset=o)
        
        for i in range(len(diagonal)-len(pattern)+1):
            if (''.join(diagonal[i:i+l]) == pattern or ''.join(diagonal[i:i+l]) == pattern_rev):
                count +=1
    return count
        

print("=================== part A ===================")
with ExecutionTimer():
    puzzle = transform_input(INPUT)
    count = find_pattern(puzzle, 'XMAS')
    print(count)
    
    # 2353
    # Execution time: 0 hours, 0 minutes, 0 seconds, 317.1482 milliseconds

print("=================== part B ===================")
with ExecutionTimer():
    puzzle = transform_input(INPUT)
    count = find_pattern_XMAS(puzzle)
    print(count)
    
    # 2353
    # Execution time: 0 hours, 0 minutes, 0 seconds, 317.1482 milliseconds