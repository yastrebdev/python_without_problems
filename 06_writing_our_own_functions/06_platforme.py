# DMOJ problem - crci07p1
# https://dmoj.ca/problem/crci07p1

def total_pillar_length(n, platforms):
    platforms.sort(reverse=True, key=lambda p: p[0])

    total_length = 0

    for i in range(n):
        y, x1, x2 = platforms[i]
        left_pillar = y
        right_pillar = y

        for j in range(i + 1, n):
            y_below, x1_below, x2_below = platforms[j]

            if x1_below < x1 < x2_below:
                left_pillar = min(left_pillar, y - y_below)

            if x1_below < x2 < x2_below:
                right_pillar = min(right_pillar, y - y_below)

        total_length += left_pillar + right_pillar

    return total_length

n = int(input())
platforms = [tuple(map(int, input().split())) for _ in range(n)]

print(total_pillar_length(n, platforms))