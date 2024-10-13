import re

# Open the file in read mode
with open("./2023/day02/input_test_1") as file:
    test_part1 = file.read().strip()

with open("./2023/day02/input_test_2") as file:
    test_part2 = file.read().strip()

with open("./2023/day02/input") as file:
    input = file.read().strip()

def calculate_good_id_sum(input):
    games=input.splitlines()

    good_id_sum = 0
    power_games_sum = 0

    for game in games:
        game_id, possible, power = analyse_game(game)
        power_games_sum += power
        if possible:
            good_id_sum += game_id
    print(f'Part 1: {good_id_sum}')
    print(f'Part 2: {power_games_sum}')


def analyse_game(game):

    game_id = int(''.join(re.findall(r'\d', game.split(":")[0])))
    game_rounds = game.split(":")[1].split(";")

    red_cubes_max = 0
    blue_cubes_max = 0
    green_cubes_max = 0
    
    for round in game_rounds:
        if "red" in round:
            color_in_round = int(re.findall(r'(\d+) red',round)[0])
            red_cubes_max = max(red_cubes_max, color_in_round)    
        if "blue" in round:
            color_in_round = int(re.findall(r'(\d+) blue',round)[0])
            blue_cubes_max = max(blue_cubes_max, color_in_round) 
        if "green" in round:
            color_in_round = int(re.findall(r'(\d+) green',round)[0])
            green_cubes_max = max(green_cubes_max, color_in_round) 

    power = red_cubes_max * green_cubes_max * blue_cubes_max
    
    return game_id, (red_cubes_max <=12 and green_cubes_max <=13 and blue_cubes_max <= 14), power

calculate_good_id_sum(test_part1)
calculate_good_id_sum(input)

# hulp van https://github.com/Hamatti/adventofcode-2023/blob/main/src/day_2.ipynb
# wat hebben we geleerd?
# 
# De regex zoekt naar een patroon 'd+ red' en retourneert enkel hetgene tussen haakjes (de cijfers d+)
# color_in_round = int(re.findall(r'(\d+) red',round)[0])