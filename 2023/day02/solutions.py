import re

# Open the file in read mode
with open("./2023/day02/input_test_1") as file:
    test_part1 = file.read().strip()

with open("./2023/day02/input_test_2") as file:
    test_part2 = file.read().strip()

with open("./2023/day02/input") as file:
    input = file.read().strip()

def calculate_possible_id_sum(input):
    games=input.splitlines()

    good_ids = 0

    for game in games:
        game_id, possible = game_is_possible(game)
        if possible:
            good_ids += game_id
    print(good_ids)


def game_is_possible(game):
    parts = re.split(':|;',game)
    
    game_id = 0
    red_cubes = 0
    blue_cubes = 0
    green_cubes = 0
    
    for part in parts:
        number = int(''.join(re.findall(r'\d', part)))
        if "Game" in part:
            game_id += number
        elif "red" in part:
            red_cubes = max(red_cubes, number)    
        elif "blue" in part:
            blue_cubes = max(green_cubes, number)  
        elif "green" in part:
            green_cubes = max(green_cubes, number)  
    
    print()
    return game_id, (red_cubes <=12 and green_cubes <=13 and blue_cubes <= 14)





# part 1
calculate_possible_id_sum(test_part1)
calculate_possible_id_sum(input)


# part 2






