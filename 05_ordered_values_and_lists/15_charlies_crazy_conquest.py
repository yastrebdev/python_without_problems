# DMOJ problem - dmopc19c5p2
# https://dmoj.ca/problem/dmopc19c5p2


moves, hp = map(int, input().split())

actions = [[], []]

charlie_hp = hp
bot_hp = hp

for i in range(2):
    for j in range(moves):
        type_action, damage = input().upper().split()
        action = (type_action, int(damage))
        actions[i].append(action)

i = 0
while i < moves:
    if actions[0][i][0] == 'A' and actions[1][i][0] == 'A':
        bot_hp -= actions[0][i][1]
        if bot_hp <= 0:
            print('VICTORY')
            break
    elif actions[0][i][0] == 'D' and actions[1][i][0] == 'D':
        charlie_hp -= actions[0][i][1]
        if charlie_hp <= 0:
            print('DEFEAT')
            break

    if actions[1][i][0] == 'A' and actions[0][i][0] == 'A':
        charlie_hp -= actions[1][i][1]
        if charlie_hp <= 0:
            print('DEFEAT')
            break
    elif actions[1][i][0] == 'D' and actions[0][i][0] == 'D':
        bot_hp -= actions[1][i][1]
        if bot_hp <= 0:
            print('VICTORY')
            break
    elif actions[1][i][0] == 'D' and actions[0][i][0] == 'D' and i == moves - 1:
        bot_hp -= actions[1][i][1]
        if bot_hp <= 0:
            print('VICTORY')
            break

    i += 1

if charlie_hp > 0 and bot_hp > 0:
    print('TIE')