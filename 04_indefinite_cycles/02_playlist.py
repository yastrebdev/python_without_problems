# DMOJ problem - ccc08j2
# https://dmoj.ca/problem/ccc08j2

songs = 'ABCDE'

button = 0
tap_count = 0

while button != 4:
    button = int(input())
    tap_count = int(input())

    for i in range(tap_count):
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]

output = ''

for song in songs:
    output += f'{song} '

print(output.strip())