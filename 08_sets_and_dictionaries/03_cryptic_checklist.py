# DMOJ problem - dmopc19c5p1
# https://dmoj.ca/problem/dmopc19c5p1

N, M = list(map(int, input().split()))

available_items = set(input().strip() for _ in range(N))

can_done = 0

for _ in range(M):
    T_i = int(input())
    required_items = set(input().strip() for _ in range(T_i))

    if required_items.issubset(available_items):
        can_done += 1

print(can_done)