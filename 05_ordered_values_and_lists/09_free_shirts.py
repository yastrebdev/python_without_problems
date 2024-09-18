# DMOJ problem - ecoo19r1p1
# https://dmoj.ca/problem/ecoo19r1p1

def washing_shirts():
    # data = input().split()
    #
    # shirts = int(data[0])
    # events = int(data[1])
    # days = int(data[2])
    shirts, events, days = map(int, input().split())

    event_days = input().split()
    event_days = [int(day) for day in event_days]

    washed_shirts = shirts
    washed = 0

    for day in range(1, days + 1):
        if washed_shirts == 0:
            washed_shirts = shirts
            washed += 1

        count_days = event_days.count(day)
        if count_days > 0:
            shirts += count_days
            washed_shirts += count_days

        washed_shirts -= 1

    print(washed)

for _ in range(10):
    washing_shirts()