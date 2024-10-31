# DMOJ problem - ccc09j2
# https://dmoj.ca/problem/ccc09j2

trout_points = int(input())
pike_points = int(input())
pickerel_points = int(input())
total_limit = int(input())

count = 0

for trout in range(total_limit // trout_points + 1):
    for pike in range(total_limit // pike_points + 1):
        for pickerel in range(total_limit // pickerel_points + 1):
            total_points = trout * trout_points + pike * pike_points + pickerel * pickerel_points
            if 0 < total_points <= total_limit:
                print(f"{trout} Brown Trout, {pike} Northern Pike, {pickerel} Yellow Pickerel")
                count += 1

print("Number of ways to catch fish:", count)