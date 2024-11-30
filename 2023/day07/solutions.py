from utils.execution_timer import ExecutionTimer
from collections import namedtuple, Counter

INPUT = './2023/day07/input'
TEST_INPUT = './2023/day07/input_test_1'

HandAndBid = namedtuple('HandAndBid', ['hand', 'bid'])

# Define card ranks (modify based on your specific rules)
CARD_RANKS_A = "23456789TJQKA"  # card ranking T: 10, J: Jack, Q: Queen, etc.
CARD_RANKS_B = "J23456789TQKA"  # ranking, J is lowest
CARD_RANK_DICT_A = {card: f"{index:02}" for index, card in enumerate(CARD_RANKS_A)}
CARD_RANK_DICT_B = {card: f"{index:02}" for index, card in enumerate(CARD_RANKS_B)}



def transform_input(inputlocation):
    with open(inputlocation) as file:
        lines = file.read().splitlines()
        camel_cards = [HandAndBid(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]
        return camel_cards
    
def first_ordering(hand):
    identical_card_with_counts = Counter(hand) # Counts occurrences of each character bv 'A':2 '2':2 T:1
    list_card_counts = identical_card_with_counts.values() # 2 2 1
    print(f'{identical_card_with_counts} - {list_card_counts}')

    
    if (5 in list_card_counts): # five of a kind
        return 7
    elif (4 in list_card_counts): # four of a kind
        return 6
    elif (3 in list_card_counts and 2 in list_card_counts): # full house
        return 5
    elif (3 in list_card_counts): # three of a kind
        return 4
    elif (Counter(list_card_counts)[2]==2): # 2 pairs
        return 3
    elif (2 in list_card_counts): # 1 pair
        return 2
    else: # all different
        return 1
    
def first_ordering_B(hand):
    identical_card_with_counts = Counter(hand) # Counts occurrences of each character bv 'A':2 '2':2 T:1
    j_count = identical_card_with_counts['J']
    
    list_other_card_counts = list(identical_card_with_counts.values())   
    if (j_count): list_other_card_counts.remove(j_count)
     
    
    print(f'{identical_card_with_counts} - j-count: {j_count} - other card count:{list_other_card_counts}')
    
    score_possibilities = [] # zonder J, met 1 J, met 2 J, met 3 J

    if (5 in list_other_card_counts): # five of a kind
        score_possibilities.append(7)
    elif (4 in list_other_card_counts): # four of a kind
        score_possibilities.extend((6, 7))
    elif (3 in list_other_card_counts and 2 in list_other_card_counts): # full house
        score_possibilities.append(5),
    elif (3 in list_other_card_counts): # three of a kind
        score_possibilities.extend((4,6,7)),
    elif (Counter(list_other_card_counts)[2]==2): # 2 pairs
        score_possibilities.extend((3,5))
    elif (2 in list_other_card_counts): # 1 pair
        score_possibilities.extend((2, 4, 6, 7))
    else: # all different
        score_possibilities.extend((1, 2, 4, 6, 7, 7))
        
    return score_possibilities[j_count]
    
def second_ordering(hand, CARD_RANK_DICT):
    # Convert each card to its rank index
    rank_for_each_card_list = [CARD_RANK_DICT[card] for card in hand]
    return ''.join(map(str, rank_for_each_card_list))
    
# Custom function to rank hands
def rank_hand(hand_and_bid):
    hand = hand_and_bid.hand
    print(f'Hand: {hand}')

    rank_1 = first_ordering(hand)
    rank_2 = second_ordering(hand, CARD_RANK_DICT_A)
    
    print(f'Rank: {str(rank_1)+rank_2}')
    
    return str(rank_1)+rank_2

# Custom function to rank hands
def rank_hand_B(hand_and_bid):
    hand = hand_and_bid.hand
    print(f'Hand: {hand}')

    rank_1 = first_ordering_B(hand)
    rank_2 = second_ordering(hand, CARD_RANK_DICT_B)
    
    print(f'Rank: {str(rank_1)+rank_2}')
    
    return str(rank_1)+rank_2


print("=================== part A ===================")
with ExecutionTimer():
    camel_cards = transform_input(INPUT)
    camel_cards_sorted = sorted(camel_cards, key=rank_hand)
    total_points = 0
    
    for index, hand_and_bid in enumerate(camel_cards_sorted):
        total_points +=  (hand_and_bid.bid)*(index+1)
        
    print(total_points)
# 250946742
# Execution time: 0 hours, 0 minutes, 0 seconds, 29.9067 milliseconds
    
print("=================== part B ===================")
with ExecutionTimer():
    camel_cards = transform_input(INPUT)
    camel_cards_sorted = sorted(camel_cards, key=rank_hand_B)
    total_points = 0
    
    for index, hand_and_bid in enumerate(camel_cards_sorted):
        total_points +=  (hand_and_bid.bid)*(index+1)
        
    print(total_points)
# 251824095
# Execution time: 0 hours, 0 minutes, 0 seconds, 45.0303 milliseconds


# Wat hebben we geleerd?
# We kunnen een custom sorted functie implementeren
# de values van de dict komen niet in een lijst, maar in een <class 'dict_values'>, waarvan ik het nut niet zo goed snap
# todo, dit kan nog serieus gerefactored worden (vraag maar aan chatgpt)










