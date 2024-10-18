import re

INPUT = './2023/day03/input'
TEST_INPUT = './2023/day03/input_test_1'

def transform_input(inputlocation):
    with open(inputlocation) as file:
        return file.read().strip().splitlines()

def find_numbers(input):
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
    return numbers

def find_symbols(input):
    symbols = {}
    for x, row in enumerate(input):
        for y, value in enumerate(row):
            if (not value.isdigit() and value != '.'):
                coordinates = (x,y)
                symbols[coordinates] = value
    return symbols

def find_numbers_near_symbols(numbers, symbols):
    numbers_near_symbol = {}
    for coordinate, value in numbers.items():
        x, y = coordinate 
        number, length_ = value 

        neighbours = find_neighbours_coordinates((x,y), length_)
    
        for neighbour in neighbours:
            if neighbour in symbols.keys():
                numbers_near_symbol[coordinate]=number, length_
                break
    return numbers_near_symbol

def find_gearsymbol_with_adjacent_partnumbers(partnumbers, gearcoordinates):
    gear_with_adjacent_partnumbers = {}

    for coordinate, value in partnumbers.items():
        x, y = coordinate 
        number, length_ = value 

        neighbours = find_neighbours_coordinates((x,y), length_)
    
        for neighbour in neighbours:
            if neighbour in gearcoordinates:
                if neighbour not in gear_with_adjacent_partnumbers:
                    gear_with_adjacent_partnumbers[neighbour] = []
                gear_with_adjacent_partnumbers[neighbour].append((coordinate, number))
                break
    return gear_with_adjacent_partnumbers



def find_neighbours_coordinates(startcoordinates, length_):
        x = startcoordinates[0] #row
        y = startcoordinates[1] #place
        neighbours = []

        for i in range(length_): 
            neighbours.append((x-1,y+i)) 
            neighbours.append((x+1,y+i)) 
            if i == 0:
                neighbours.append((x-1,y-1))
                neighbours.append((x,y-1))
                neighbours.append((x+1,y-1))
            if i == length_-1:
                neighbours.append((x-1,y+i+1))
                neighbours.append((x,y+1+i))
                neighbours.append((x+1,y+1+i))
        return neighbours

def find_gear_symbols(symbols):
    gear_symbols=[]

    for coordinates, value in symbols.items():
        x, y = coordinates
        if (value == '*'):
            gear_symbols.append(coordinates)
    return gear_symbols


input_list = transform_input(INPUT)

print("=================== part A ===================")
numbers_dict = find_numbers(input_list)
symbols_dict = find_symbols(input_list)
partnumber_dict = find_numbers_near_symbols(numbers_dict, symbols_dict)

sum = 0
for partnumber in partnumber_dict.values():
    sum += partnumber[0]

print(sum)

print("=================== part B ===================")
gear_symbols_coordinate_list = find_gear_symbols(symbols_dict)
gear_with_adjacent_partnumbers_dict = find_gearsymbol_with_adjacent_partnumbers(partnumber_dict, gear_symbols_coordinate_list)

sum = 0
for gear in gear_with_adjacent_partnumbers_dict.values():
    
    if (len(gear) == 2):
        sum += gear[0][1]*gear[1][1]

print(sum)











                




# https://adventofcode.com/2023/day/3
# https://github.com/fuglede/adventofcode/blob/master/2023/day03/solutions.py
# https://github.com/Hamatti/adventofcode-2023/blob/main/src/day_3.ipynb
# https://github.com/nitekat1124/advent-of-code-2023/blob/main/solutions/day03.py



