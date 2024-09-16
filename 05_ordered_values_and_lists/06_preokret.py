# DMOJ problem - coci18c2p1
# https://dmoj.ca/problem/coci18c2p1


def get_data_match():
    first_half_points = 0
    turnarounds_count = 0

    events = []

    for command in ['A', 'B']:
        points = int(input())
        for i in range(points):
            seconds = int(input())
            if seconds <= 1440:
                first_half_points += 1
            events.append([seconds, command])

    events.sort()

    score = {'A': 0, 'B': 0}
    leading_team = ''

    for _, team in events:
        if team == 'A':
            score['A'] += 1
            if score['A'] > score['B']:
                if leading_team != 'A' and leading_team != '':
                    turnarounds_count += 1
                leading_team = 'A'
        else:
            score['B'] += 1
            if score['B'] > score['A']:
                if leading_team != 'B' and leading_team != '':
                    turnarounds_count += 1
                leading_team = 'B'

    print(first_half_points)
    print(turnarounds_count)


get_data_match()