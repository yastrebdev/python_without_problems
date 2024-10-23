# DMOJ problem - dmopc19c3p1
# https://dmoj.ca/problem/dmopc19c3p1

def read_numbers():
    n = int(input())
    numbers = list(map(int, input().split()))

    return numbers


numbers = read_numbers()

frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_frequency = max(frequency.values())

modes = []
for num, freq in frequency.items():
    if freq == max_frequency:
        modes.append(num)

modes.sort()
print(*modes)