# DMOJ problem - ccc06j1
# https://dmoj.ca/problem/ccc06j1

position_1 = int(input())
position_2 = int(input())
position_3 = int(input())
position_4 = int(input())

calories = 0

if position_1 == 1:
    calories += 461
elif position_1 == 2:
    calories += 431
elif position_1 == 3:
    calories += 420
else:
    calories += 0

if position_2 == 1:
    calories += 100
elif position_2 == 2:
    calories += 57
elif position_2 == 3:
    calories += 70
else:
    calories += 0

if position_3 == 1:
    calories += 130
elif position_3 == 2:
    calories += 160
elif position_3 == 3:
    calories += 118
else:
    calories += 0

if position_4 == 1:
    calories += 167
elif position_4 == 2:
    calories += 266
elif position_4 == 3:
    calories += 75
else:
    calories += 0

print('Your total Calorie count is', str(calories) + '.')