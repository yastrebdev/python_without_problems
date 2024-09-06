# DMOJ problem - ccc00s1
# https://dmoj.ca/problem/ccc00s1

coins = int(input())

slot1 = int(input())
slot2 = int(input())
slot3 = int(input())

plays = 0

while coins >= 1:
    machine = plays % 3
    coins -= 1

    if machine == 0:
        slot1 += 1
        if slot1 % 35 == 0:
            coins += 30
    elif machine == 1:
        slot2 += 1
        if slot2 % 100 == 0:
            coins += 60
    elif machine == 2:
        slot3 += 1
        if slot3 % 10 == 0:
            coins += 9

    plays += 1

print(f'Martha plays {plays} times before going broke.')