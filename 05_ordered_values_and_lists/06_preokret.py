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
    leading_team = None

    for _, team in events:
        score[team] += 1

        other_team = 'B' if team == 'A' else 'A'
        if score[team] > score[other_team]:
            if leading_team != team:
                if leading_team:
                    turnarounds_count += 1
                leading_team = team

    print(first_half_points)
    print(turnarounds_count)


get_data_match()