# DMOJ problem - ccc15j1
# https://dmoj.ca/problem/ccc15j1

month = int(input())
day = int(input())

if (month == 2 and day > 18) or month > 2:
    print('After')
elif (month == 2 and day < 18) or month < 2:
    print('Before')
else:
    print('Special')