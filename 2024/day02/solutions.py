from utils.execution_timer import ExecutionTimer
from collections import namedtuple, Counter
# import numpy as np

INPUT = './2024/day02/input'
TEST_INPUT = './2024/day02/input_test'

def transform_input(inputlocation):
    with open(inputlocation) as file:
        input = file.read().splitlines()
        reports = [list(map(int, report.split())) for report in input]
        return reports
    
def is_report_safe(report):
    
    order = 'INCREASING' if (report[1]-report[0]) > 0 else 'DECREASING'
    
    # Check if all differences between consecutive numbers meet the condition
    if order == 'INCREASING':
        return all(0 < report[i] - report[i - 1] <= 3 for i in range(1, len(report)))
    else:
        return all(0 < report[i - 1] - report[i] <= 3 for i in range(1, len(report)))
    
def is_report_safe_with_dampener(report):
    
    if is_report_safe(report):
        return True
    else:
        for i in range(0, len(report)):
            report_dampened = report.copy()
            del report_dampened[i]
            
            if is_report_safe(report_dampened):
                return True
    return False
            
    

print("=================== part A ===================")
with ExecutionTimer():
    reports = transform_input(INPUT) 
    safe_reports_counter = sum(is_report_safe(report) for report in reports)
    print(safe_reports_counter)

# 314
# Execution time: 0 hours, 0 minutes, 0 seconds, 3.1285 milliseconds
    
    

print("=================== part B ===================")
with ExecutionTimer():
    safe_reports_counter = sum(is_report_safe_with_dampener(report) for report in reports)
    print(safe_reports_counter)
    
# 373
# Execution time: 0 hours, 0 minutes, 0 seconds, 7.3190 milliseconds











