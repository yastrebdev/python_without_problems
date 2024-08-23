# DMOJ problem - coci16c1p1
# https://dmoj.ca/problem/coci16c1p1

x = int(input())
m = int(input())

mb = x

for i in range(m):
    n = int(input())
    remains = x - n
    mb += remains

print(mb)