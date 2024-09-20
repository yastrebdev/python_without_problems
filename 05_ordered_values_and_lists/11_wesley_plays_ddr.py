# DMOJ problem - wac3p3
# https://dmoj.ca/problem/wac3p3

sequence = input().upper()
combos_count = int(input())

len_sequence = len(sequence)

combos = []
score = len_sequence

for _ in range(combos_count):
    combo = input().upper().split()
    if combo[0] not in sequence:
        continue
    else:
        combos.append(combo)

if len(combos) == 1:
    score += int(combos[0][1])
elif len(combos) == 0:
    score += len_sequence
else:
    combos.sort(key=lambda c: len(c[0]), reverse=True)

    move = 0
    while move < len_sequence:
        for combo, points in combos:
            if move + len(combo) <= len_sequence and sequence[move:len(combo) + move] == combo:
                score += int(points)
                move += len(combo)

        move += 1

print(score)