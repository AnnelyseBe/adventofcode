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

print(min(locations)) # 535088217

print("=================== part B ===================")

# Initieel had ik gewoon dezelfde manier gebruikt als deel A. Dit lukte ergens niet, zoveel waarden in de seeds lijst zetten deed mijn pc crashen.

# Ik ben gegaan voor de lazy oplossing en ipv alle waarden in een lijst te zetten, loop ik apart over alle waarden in de range, zonder ze eerst in een lijst te zetten. 
# En telkens verifieren of de location kleiner is dan de waarde die al in het geheugen zat
# dan heb je minder geheugen plaatsen nodig en werk je 1 per 1 af.
# Dit lukte, maar mijn computer had er meer dan 3u voor nodig (maar hij crashte tenminste niet meer)

# De betere oplossing is starten van de locatie = 0. En dan checken of de overeenkomstige seed in onze seeds zit (dat zou op een 2 tal minuten mogen duren)

min_location = calculate_seed_to_location(seeds[0], ranges)
for i in range(0, len(seeds), 2):
    for seed in (range(seeds[i], seeds[i] + seeds[i+1])):
        location = calculate_seed_to_location(seed, ranges)
        min_location = location if location < min_location else min_location
    
print(min_location)  # 51399228

print("============== calculation time ==============")

end_time = time.time()
execution_time = end_time - start_time

print(f'Execution time: {execution_time:.4f} seconds')


# Execution time: 11448.0472 seconds






