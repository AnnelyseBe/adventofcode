import re
from collections import namedtuple
import time

start_time = time.time()


INPUT = './2023/day05/input'
TEST_INPUT = './2023/day05/input_test_1'

Range_ = namedtuple("Conversion", ["dest_start", "source_start", "range_lenght"])

def transform_input(inputlocation):
    with open(inputlocation) as file:
        return file.read().split('\n\n')

def extract_seeds(almanac_paragraphs):
    seeds = [int(seed) for seed in re.findall(r'\d+', almanac_paragraphs[0])]
    return seeds

def extract_ranges(paragraph):
    conversion_ranges=[]

    lines = paragraph.split('\n')
    
    for line in lines[1:]:
        range_numbers = [int(range_numbers) for range_numbers in re.findall(r'(\d+)', line)]
        conversion_ranges.append(Range_(*range_numbers))

    return conversion_ranges


def calculate_conversion(start_value, conversion_ranges):
    conversion=start_value
    for range in conversion_ranges:
        if (start_value >= range.source_start and start_value < range.source_start + range.range_lenght):
            return range.dest_start + (start_value - range.source_start)
    return start_value

def calculate_seed_to_location(seed, ranges):
    temp_value = seed
    for conversion_ranges in ranges:
        temp_value = calculate_conversion(temp_value, conversion_ranges)
    return temp_value

def to_seed_ranges_approach(seeds):
    complete_seed_list = []
    for i in range(0, len(seeds), 2):
        complete_seed_list.extend(range(seeds[i], seeds[i] + seeds[i+1]))
    return complete_seed_list



print("=================== part A ===================")
almanac_paragraphs = transform_input(INPUT)

seeds = extract_seeds(almanac_paragraphs)
print(len(seeds))

seed_to_soil = extract_ranges(almanac_paragraphs[1])
soil_to_fertilizer = extract_ranges(almanac_paragraphs[2])
fertilizer_to_water = extract_ranges(almanac_paragraphs[3])
water_to_light = extract_ranges(almanac_paragraphs[4])
light_to_temperature = extract_ranges(almanac_paragraphs[5])
temperature_to_humidity = extract_ranges(almanac_paragraphs[6])
humidity_to_location = extract_ranges(almanac_paragraphs[7])

ranges = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location
]

locations = [calculate_seed_to_location(seed, ranges) for seed in seeds]

print(min(locations))

print("=================== part B ===================")

# dit mag ik echt niet runnen. Te groot en laat mijn computer crashen. Ik las ergens dat je moet terugrekenen. Kleinste locatie (=0) terugrekenen naar seedgetal en dan verifieren of dat in onze seeds zit.
# dan zou het nog 2 min ofzo duren
# ik zou denken dat we best de seed opdelen in reeksen van 1000 ofzo en telkens de berekening laten doen -> dan zal het wel super lang duren

# complete_seed_list = to_seed_ranges_approach(seeds) 

# locations_complete_seed_list = []

# for seed in complete_seed_list:
#     locations_complete_seed_list.append(calculate_seed_to_location(seed, ranges))

# print(min(locations_complete_seed_list))

print("============== calculation time ==============")

end_time = time.time()
execution_time = end_time - start_time

print(f'Execution time: {execution_time:.2f} seconds')






