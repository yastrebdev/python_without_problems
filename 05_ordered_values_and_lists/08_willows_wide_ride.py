# DMOJ problem - ecoo18r1p1
# https://dmoj.ca/problem/ecoo18r1p1


def playing_with_box():
    all_days = input().split()

    playing_days = 0

    for _ in range(int(all_days[1])):
        action = input().upper()

        if action == 'E':
            if playing_days > 0:
                playing_days -= 1
        elif action == 'B':
            playing_days += int(all_days[0])
            playing_days -= 1

    print(playing_days)


playing_with_box()