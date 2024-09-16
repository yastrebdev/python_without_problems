# DMOJ problem - coci17c1p1
# https://dmoj.ca/problem/coci17c1p1

deck = [4, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]

hand = int(input())

values = []
for _ in range(hand):
    value = int(input())
    values.append(value)
    deck[value - 1] -= 1

if sum(values) >= 21:
    print('DOSTA')
else:
    difference = 21 - sum(values)
    if sum(deck[difference:]) >= sum(deck[:difference]):
        print('DOSTA')
    else: print('VUCI ')