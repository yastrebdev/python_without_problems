# DMOJ problem - crci06p1
# https://dmoj.ca/problem/crci06p1

def write_input_data():
    n = int(input())
    e = int(input())

    evening = []
    for _ in range(e):
        residents = set(map(int, input().split()[1:]))
        evening.append(residents)

    all_residents = {}
    for i in range(n):
        all_residents[i + 1] = 0

    return evening, all_residents


evening, all_residents = write_input_data()

all_songs = 0
for e in evening:
    if 1 in e:
        all_songs += 1
        for r in e:
            all_residents[r] += 1
    else:
        for r in e:
            if all_residents[r] == all_songs:
                for res in e:
                    if all_residents[res] == all_songs:
                        continue
                    else:
                        all_residents[res] += 1

for key, value in all_residents.items():
    if value == all_songs:
        print(int(key))