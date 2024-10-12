import re

# Open the file in read mode
with open("./2023/day01/input_test_1") as file:
    test_part1 = file.read().strip()

with open("./2023/day01/input_test_2") as file:
    test_part2 = file.read().strip()

with open("./2023/day01/input") as file:
    my_calibration_document = file.read().strip()

def calibration(calibration_document):
    lines=calibration_document.splitlines()

    calibration_result = 0
    for line in lines:
        digits_only = ''.join(re.findall(r'\d',line))
        calibration_values = int(digits_only[0] + digits_only[-1])
        calibration_result = calibration_result + calibration_values
    print(calibration_result)

def prepare_input(calibration_document_raw):
    cleaned_document = (calibration_document_raw
        .replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine"))
    return cleaned_document

# part 1
calibration(test_part1)
calibration(my_calibration_document)


# part 2
calibration(prepare_input(test_part2))
calibration(prepare_input(my_calibration_document))





