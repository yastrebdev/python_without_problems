# DMOJ problem - coci18c4p1
# https://dmoj.ca/problem/coci18c4p1

wizard = input()
duels = int(input())

owner_counter = 1
owners = [wizard]

for i in range(duels):
    duel = input()
    duel_list = duel.split(' ')

    if duel_list[1] == wizard:
        wizard = duel_list[0]
        if wizard in owners:
            continue
        else:
            owner_counter += 1
            owners.append(wizard)

print(wizard)
print(owner_counter)