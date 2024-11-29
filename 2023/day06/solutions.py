from utils.execution_timer import ExecutionTimer
import re
from collections import namedtuple

INPUT = './2023/day06/input'
TEST_INPUT = './2023/day06/input_test_1'

Race = namedtuple('Race', ['time', 'distance'])

def transform_input(inputlocation):
    with open(inputlocation) as file:
        input_lines = file.read().split("\n")
        
        race_times = re.findall(r"\d+",input_lines[0])
        race_times = [int(num) for num in race_times]  # Convert to integers
        
        race_distances = re.findall(r"\d+",input_lines[1])
        race_distances = [int(num) for num in race_distances]  # Convert to integers
        
        # Create named tuples and store them in a list
        races = [Race(time, distance) for time, distance in zip(race_times, race_distances)]
        return races
    
def transform_input_b(inputlocation):
    with open(inputlocation) as file:
        input_lines = file.read().split("\n")
        
        race_time = ''.join(re.findall(r'\d',input_lines[0]))
        race_time = int(race_time) # Convert to integers
        
        race_distance = ''.join(re.findall(r'\d',input_lines[1]))
        race_distance = int(race_distance)  # Convert to integers
        
        # Create named tuples and store them in a list
        race = Race(race_time, race_distance)
        return race
    

    
def calculate_distance(race_time, hold_time):
    distance = (race_time - hold_time) * hold_time
    # print(f'hold time: {hold_time} - distance: {distance}')
    return distance

print("=================== part A ===================")
with ExecutionTimer():
    races = transform_input(INPUT)

    win_possibilities_races = []
    
    for race in races:
        print(race)
        win_possibilities = 0
        for hold_time in range(1, race.time):
            if calculate_distance(race.time, hold_time) > race.distance:
                win_possibilities += 1
        win_possibilities_races.append(win_possibilities)
    
    total_possibilities = 1
    for race in win_possibilities_races:
        total_possibilities *= race
        
    print(total_possibilities) # 588588
    
print("=================== part B ===================")
with ExecutionTimer():
    race = transform_input_b(INPUT)
    
    win_possibilities = 0

    print(race)
    for hold_time in range(1, race.time):
        if calculate_distance(race.time, hold_time) > race.distance:
            win_possibilities += 1   
            print(win_possibilities) 
       

    print(win_possibilities) 
    # 34655848
    # Execution time: 0 hours, 3 minutes, 59 seconds, 742.5604 milliseconds
    # Execution time: 0 hours, 0 minutes, 7 seconds, 822.0492 milliseconds -> zonder in elke loop te printen. Conclusie 'print neemt veel tijd)








