# DMOJ problem - dmopc14c7p2
# https://dmoj.ca/problem/ecoo19r1p1


def get_difference():
    # actions = int(input())
    values = list(map(int, input().split()))

    min_value_index = values.index(min(values))
    max_value_index = values.index((max(values)))

    sequence = values[min_value_index:max_value_index + 1]

    if len(sequence) == 0:
        result = 'unknown'
    else:
        result = sequence[-1] - sequence[0]

    for i in range(len(sequence)):
        if i == 0: continue

        if sequence[i] < sequence[i - 1]:
            result = 'unknown'
            break

    print(result)


get_difference()