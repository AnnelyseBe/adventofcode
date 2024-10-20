import re
from collections import namedtuple

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
            conversion = range.dest_start + (start_value - range.source_start)
            break
    return conversion

def calculate_seed_to_location(seed, ranges):
    temp_value = seed
    for conversion_ranges in ranges:
        temp_value = calculate_conversion(temp_value, conversion_ranges)
    return temp_value



print("=================== part A ===================")
almanac_paragraphs = transform_input(INPUT)
seeds = extract_seeds(almanac_paragraphs)

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

locations = []

for seed in seeds:
    locations.append(calculate_seed_to_location(seed, ranges))

print(min(locations))






