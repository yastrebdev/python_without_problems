# DMOJ problem - ecoo13r1p1
# https://dmoj.ca/problem/ecoo13r1p1

next_number = int(input())

take = 0
serve = 0

while True:
    action = input().strip()

    if action == 'EOF':
        break

    if action == 'TAKE':
        take += 1
        serve += 1
        next_number += 1
        if next_number > 999:
            next_number = 1
    elif action == 'SERVE':
        if serve > 0:
            serve -= 1
    elif action == 'CLOSE':
        print(f'{take} {serve} {next_number}')

        take = 0
        serve = 0