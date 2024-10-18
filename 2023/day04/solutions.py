import re
from collections import namedtuple

INPUT = './2023/day04/input'
TEST_INPUT = './2023/day04/input_test_1'
Scratchcard = namedtuple('Scratchcard', ['card_number', 'winning_numbers', 'my_numbers', 'score', 'matches'])

def transform_input(inputlocation):
    with open(inputlocation) as file:
        lines = file.read().strip().splitlines()

        cards = []
        
        for line in lines:
            
            card_part = line.split(':')[0]
            winning_part = line.split(':')[1].split('|')[0].strip()
            my_numbers_part = line.split(':')[1].split('|')[1].strip()

            card_number = int(''.join(re.findall(r'\d',card_part)))
            winning_numbers = winning_part.split()
            my_numbers = my_numbers_part.split()

            cards.append(Scratchcard(card_number, winning_numbers, my_numbers, 0, 0))

        return cards    

        
def calculate_card_points(scratchcards):
    
    scratchcards_with_score = []
    
    for card in scratchcards:
        my_wins = [x for x in card.my_numbers if x in card.winning_numbers] # list comprehension
        power = len(my_wins)-1
        score = 0 if len(my_wins) == 0 else 2 ** power
        # Create a new namedtuple with updated score
        updated_card = Scratchcard(card.card_number, card.winning_numbers, card.my_numbers, score, len(my_wins))
        scratchcards_with_score.append(updated_card)

    return scratchcards_with_score

def calculate_cart_count(scratchcards):
    cards_count = {i:1 for i in range(1,len(scratchcards)+1)}
    print(cards_count)

    for card in scratchcards: 
        for i in range(card.matches):
            cards_count[card.card_number + 1 + i] += cards_count[card.card_number]

    print(cards_count)
    return cards_count


print("=================== part A ===================")
scratchcards = transform_input(INPUT)
scratchcards = calculate_card_points(scratchcards)
sum = 0

for card in scratchcards:
    sum += card.score

print(sum)


print("=================== part B ===================") 
cards_count = calculate_cart_count(scratchcards)

sum = 0
for card in cards_count.values():
    sum += card

print(sum)


# https://www.squash.io/how-to-compare-two-lists-in-python-and-return-matches/