# DMOJ problem - ccc99s1
# https://dmoj.ca/problem/ccc99s1

NUMBER_CARDS = 52


def no_senior(cards):
    """
    :param cards: это список строк, соответствующих картам
    :return True: если в cards нет старших карт
    :return False: в остальных случаях
    """
    
    if 'jack' in cards:
        return False
    if 'queen' in cards:
        return False
    if 'king' in cards:
        return False
    if 'ace' in cards:
        return False
    else: return True


deck = []
for _ in range(NUMBER_CARDS):
    deck.append(input())

score_a = 0
score_b = 0
player = 'A'

for i in range(NUMBER_CARDS):
    card = deck[i]
    points = 0
    remaining = NUMBER_CARDS - i - 1

    if card == 'jack' and no_senior(deck[i + 1:i + 2]) and remaining >= 1:
        points = 1
    elif card == 'queen' and no_senior(deck[i + 1:i + 3]) and remaining >= 2:
        points = 2
    elif card == 'king' and no_senior(deck[i + 1:i + 4]) and remaining >= 3:
        points = 3
    elif card == 'ace' and no_senior(deck[i + 1:i + 5]) and remaining >= 4:
        points = 4

    if points > 0:
        print(f'Player {player} scores {points} point(s).')

    if player == 'A':
        score_a += points
        player = 'B'
    else:
        score_b += points
        player = 'A'

print(f'Player A: {score_a} point(s).')
print(f'Player B: {score_b} point(s).')