# DMOJ problem - ccc13s1
# https://dmoj.ca/problem/ccc13s1

def check_duplicates(y):
    y = str(y)
    for n in y:
        if y.count(n) > 1:
            return True
        else:
            continue

    return False

year = int(input()) + 1

while check_duplicates(year):
    year += 1

print(year)