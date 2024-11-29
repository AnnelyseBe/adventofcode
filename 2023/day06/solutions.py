from utils.execution_timer import ExecutionTimer
import re
import os


print(os.listdir())

INPUT = './2023/day06/input'
TEST_INPUT = './2023/day06/input_test_1'

def transform_input(inputlocation):
    with open(inputlocation) as file:
        input_lines = file.read().split("\n\n")
        race_time = re.split(r"\D+",input_lines[0])
        race_distance = re.split(r"\D+",input_lines[1])
        return race_time, race_distance


print("=================== part A ===================")
with ExecutionTimer():
    race_time, race_distance = transform_input(TEST_INPUT)
    print(race_time)
    print(race_distance)
        




print("=================== part B ===================")









