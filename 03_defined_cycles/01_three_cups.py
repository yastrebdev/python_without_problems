# DMOJ problem - coci06c5p1
# https://dmoj.ca/problem/coci06c5p1

position_list = input()
ball_position = 1

for i in position_list:
    if i == 'A' and ball_position == 1:
        ball_position = 2
    elif i == 'A' and ball_position == 2:
        ball_position = 1
    elif i == 'B' and ball_position == 2:
        ball_position = 3
    elif i == 'B' and ball_position == 3:
        ball_position = 2
    elif i == 'C' and ball_position == 1:
        ball_position = 3
    else:
        ball_position = 1

print(ball_position)