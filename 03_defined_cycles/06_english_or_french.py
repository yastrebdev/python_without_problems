# DMOJ problem - ccc11s1
# https://dmoj.ca/problem/ccc11s1

n = int(input())

t_count = 0
s_count = 0

for i in range(n):
    line = input().lower()
    t_count += line.count('t')
    s_count += line.count('s')

if t_count > s_count:
    print('English')
else: print('French')