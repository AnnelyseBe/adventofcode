from utils.execution_timer import ExecutionTimer
from collections import Counter

INPUT = './2024/day01/input'
TEST_INPUT = './2024/day01/input_test'

def transform_input(inputlocation):
    with open(inputlocation) as file:
        lines = file.read().splitlines()
        list_1 = [int(line.split()[0]) for line in lines]
        list_2 = [int(line.split()[1]) for line in lines]
        return list_1, list_2

print("=================== part A ===================")
with ExecutionTimer():
    list_1, list_2 = transform_input(INPUT)
    list_1.sort()
    list_2.sort()
    distance = 0
    
    for i in range(len(list_1)):
        distance += abs(list_1[i]-list_2[i])
        
    print(distance)
    
    # 765748
    # Execution time: 0 hours, 0 minutes, 0 seconds, 1.0792 milliseconds
    
print("=================== part B ===================")
with ExecutionTimer():
    
    similarity_score = 0
    list_2_occurences = Counter(list_2)
    
    for number in list_1:
        occurence_count = list_2_occurences.get(number, 0)
        similarity_score += number * occurence_count
    
    print(similarity_score)
    
    # 27732508
    # Execution time: 0 hours, 0 minutes, 0 seconds, 0.2154 milliseconds