# DMOJ problem - ecoo19r1p1
# https://dmoj.ca/problem/ecoo19r1p1
# TODO Обработать несколько мероприятий в 1 день

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

        if day in event_days:
            shirts += 1
            washed_shirts += 1

        washed_shirts -= 1

    print(washed)

for _ in range(10):
    washing_shirts()