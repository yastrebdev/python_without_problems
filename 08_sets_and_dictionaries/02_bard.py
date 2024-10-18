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

data_by_songs = set()
for e in evening:
    if 1 in e:
        data_by_songs.update(e)
    else:
        for r in e:
            if r in data_by_songs and r in e:
                data_by_songs.update(e)

list_songs = list(data_by_songs)
list_songs.sort()

for song in list_songs:
    print(song)