# DMOJ problem - coci20c1p1
# https://dmoj.ca/problem/coci20c1p1

CARDINAL_DIRECTIONS = {
    '^': 'N',
    'v': 'S',
    '<': 'W',
    '>': 'E'
}

def read_input(r):
    o = None
    x = None

    ocean = [[] for _ in range(r)]

    for i in range(r):
        row = input()
        for char in row:
            if char == 'o':
                o = (i, row.index(char))
            elif char == 'x':
                x = (i, row.index(char))

            ocean[i].append(char)

    return o, x, ocean


def possible_directions(ocean, o, r, s):
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    row, col = o

    routes = ''
    min_moves = 0

    for key, value in directions.items():
        dr, dc = value
        new_row, new_col = row + dr, col + dc

        moves = 0

        if 0 <= new_row < r and 0 <= new_col < s:
            while True:
                if ocean[new_row][new_col] == '.':
                    break
                elif ocean[new_row][new_col] == 'x':
                    curr_dir = CARDINAL_DIRECTIONS[key]
                    if min_moves == 0 or min_moves > moves:
                        min_moves = moves
                        routes = f'{curr_dir} '
                    elif min_moves == moves:
                        routes += f'{curr_dir} '
                    break
                else:
                    if ocean[new_row][new_col] in directions:
                        xc, yc = directions[ocean[new_row][new_col]]
                        new_row += xc
                        new_col += yc
                        moves += 1
                    else:
                        break

    return routes.strip()


r, s = list(map(int, input().split()))
o, x, ocean = read_input(r)

routes = possible_directions(ocean, o, r, s)
routes = routes.split()
routes.sort()

if bool(routes):
   print(':)')
   print(routes[0])
else:
    print(':(')