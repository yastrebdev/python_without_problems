# DMOJ problem - coci14c2p2
# https://dmoj.ca/problem/coci14c2p2

from collections import Counter


def find_missing_participant(start, finish):
    counter = Counter(start)

    for name in finish:
        counter[name] -= 1

    for name, count in counter.items():
        if count > 0:
            return name


n = int(input())
start = [input().strip() for _ in range(n)]
finish = [input().strip() for _ in range(n - 1)]

missing_participant = find_missing_participant(start, finish)
print(missing_participant)