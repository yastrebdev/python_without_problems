# DMOJ problem - coci20c2p1
# https://dmoj.ca/problem/dmopc20c2p1

chars_count = int(input())
chars = input()

grid = [['.' for i in range(chars_count)]]

y = 0
x = 0

for i, char in enumerate(chars):
    if char == 'v':
        y += 1

        if y == len(grid):
            grid.append(['.' for i in range(chars_count)])

        grid[y][x] = '\\'

    elif char == '>':
        grid[y][x] = '_'

    elif char == '^':
        grid[y][x] = '/'

        y -= 1

        if y < 0:
            grid.insert(0, ['.' for i in range(chars_count)])
            y = 0

    x += 1

for row in grid:
    if row.count('.') == chars_count:
        continue

    print(''.join(row))