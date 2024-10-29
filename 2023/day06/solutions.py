import re
from collections import namedtuple
import time

start_time = time.time()


INPUT = './2023/day06/input'
TEST_INPUT = './2023/day06/input_test_1'

def transform_input(inputlocation):
    with open(inputlocation) as file:
        return file.read().split('\n\n')






print("=================== part A ===================")
almanac_paragraphs = transform_input(TEST_INPUT)


print("=================== part B ===================")



print("============== Execution time ==============") # Execution time: 

end_time = time.time()
execution_time = end_time - start_time

hours, rem = divmod(execution_time, 3600)
minutes, rem = divmod(rem, 60)
seconds, milliseconds = divmod(rem, 1)
milliseconds *= 1000

print(f"Execution time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds, {milliseconds:.4f} milliseconds")









