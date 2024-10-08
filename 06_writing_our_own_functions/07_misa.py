# DMOJ problem - coci13c2p2
# https://dmoj.ca/problem/coci13c2p2

def count_touches_from_position(matrix, row, col):
    rows = len(matrix)
    cols = len(matrix[0])
    touches = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for d in directions:
        ni, nj = row + d[0], col + d[1]
        if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] == 'o':
            touches += 1

    return touches


def find_best_position(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_touches = -1

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '.':
                touches = count_touches_from_position(matrix, i, j)
                if touches > max_touches:
                    max_touches = touches

    return max_touches


r, s = map(int, input().split())
rows = [list(input()) for _ in range(r)]

print(find_best_position(rows))