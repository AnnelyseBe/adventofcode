import re

INPUT = './2023/day03/input'
TEST_INPUT = './2023/day03/input_test_1'

def transform_input(inputlocation):
    with open(inputlocation) as file:
        return file.read().strip().splitlines()

def findNumbers(input):
    numbers = {}
    for x, row in enumerate(input):
        temp_number = ''
        coordinates = ''
        for y, value in enumerate(row):
            if value.isdigit() and len(temp_number) == 0:
                coordinates = (x,y)
                temp_number += value
            elif value.isdigit():
                temp_number += value

            if (not value.isdigit() or (y == len(row)-1)) and len(temp_number) != 0:
                numbers[coordinates] = int(temp_number) , len(temp_number)
                coordinates = ''
                temp_number = ''
    print(numbers)
    return numbers

def findSymbols(input):
    symbols = {}
    for x, row in enumerate(input):
        for y, value in enumerate(row):
            if (not value.isdigit() and value != '.'):
                coordinates = (x,y)
                symbols[coordinates] = value
    print(symbols)
    return symbols

def findPartNumbers(numbers, symbols):
    partnumbers = {}
    for coordinate, value in numbers.items():
        x, y = coordinate #rij 0 pos0
        number, length_ = value # 5, 1

        neighbours = []

        for i in range(length_): # 0,1
            neighbours.append((x-1,y+i)) #1,2
            # neighbours.append((x,y+i))   #2,2
            neighbours.append((x+1,y+i)) #3,2
            if i == 0:
                neighbours.append((x-1,y-1))
                neighbours.append((x,y-1))
                neighbours.append((x+1,y-1))
            if i == length_-1:
                neighbours.append((x-1,y+i+1))
                neighbours.append((x,y+1+i))
                neighbours.append((x+1,y+1+i))
    

        for neighbour in neighbours:
            if neighbour in symbols.keys():
                partnumbers[coordinate]=number
                break
    print(partnumbers)
    return partnumbers

def find_gears(numbers, symbols, input):
    gear_symbols={}

    for coordinates, value in symbols.items():
        x, y = coordinates
        if (value == '*'):
            gear_symbols[coordinates]=(value)
    print("======gearsymbol=======")
    print(gear_symbols)

    # zoek parts links, rechts, boven en onder
    # part links -> bereken laatste coordinaat en check naast
    # part rechts -> naast gear?
    # part boven -> 







def calculate_partnumber_sum(input):
    print("========numbers=====================")
    numbers = findNumbers(input)
    print("========symbols=====================")
    symbols = findSymbols(input)
    print("========partnumbers=====================")
    partnumbers = findPartNumbers(numbers, symbols)
    print("========sum=====================")
    sum = 0
    for partnumber in partnumbers.values():
        sum += partnumber
    print(sum)
    find_gears(numbers, symbols, input)
    

calculate_partnumber_sum(transform_input(INPUT))







                




# https://adventofcode.com/2023/day/3
# https://github.com/fuglede/adventofcode/blob/master/2023/day03/solutions.py
# https://github.com/Hamatti/adventofcode-2023/blob/main/src/day_3.ipynb
# https://github.com/nitekat1124/advent-of-code-2023/blob/main/solutions/day03.py



