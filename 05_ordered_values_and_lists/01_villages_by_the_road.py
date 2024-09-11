# DMOJ problem - ccc18s1
# https://dmoj.ca/problem/ccc18s1

villages_count = int(input())

villages = []
for _ in range(villages_count):
    village = int(input())
    villages.append(village)

villages.sort()

s = []
for i in range(len(villages)):
    if i == 0 or i == len(villages) - 1:
        continue

    left = (villages[i] - villages[i - 1]) / 2
    right = (villages[i + 1] - villages[i]) / 2
    result = right + left
    s.append(result)

print(min(s))