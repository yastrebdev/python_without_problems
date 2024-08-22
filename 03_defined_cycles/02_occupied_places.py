# DMOJ problem - ccc18j2
# https://dmoj.ca/problem/ccc18j2

n = int(input())

yesterday  = input()
today  = input()

occupied  = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied += 1

print(occupied)