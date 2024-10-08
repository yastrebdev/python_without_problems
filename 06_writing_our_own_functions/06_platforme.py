# DMOJ problem - crci07p1
# https://dmoj.ca/problem/crci07p1

def total_pillar_length(n, platforms):
    platforms.sort(reverse=True, key=lambda p: p[0])
    total_length = 0

    for i in range(n):
        y, x1, x2 = platforms[i]
        if i == n -1:
            total_length += y * 2
            break

        for x in ['x1', 'x2']:
            for j in range(i + 1, n):
                ly, lx1, lx2 = platforms[j]
                if x == 'x1':
                    if x1 < lx1:
                        if j == n - 1:
                            total_length += y
                        else:
                            continue
                    else:
                        total_length += y - ly
                        break

                if x == 'x2':
                    if x2 > lx2:
                        if j == n - 1:
                            total_length += y
                        else:
                            continue
                    elif x2 <= lx2:
                        if x2 <= lx1:
                            total_length += y
                        else:
                            total_length += y - ly
                    else:
                        total_length += y - ly
                        break

    return total_length

n = int(input())
platforms = [list(map(int, input().split())) for _ in range(n)]

print(total_pillar_length(n, platforms))