# DMOJ problem - ccc07j1
# https://dmoj.ca/problem/ccc07j1

v1 = int(input())
v2 = int(input())
v3 = int(input())

if (v2 < v1 < v3) or (v2 > v1 > v3):
    print(v1)
elif (v1 < v2 < v3) or (v1 > v2 > v3):
    print(v2)
else:
    print(v3)