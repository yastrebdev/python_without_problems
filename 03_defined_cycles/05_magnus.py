# DMOJ problem - coci18c3p1
# https://dmoj.ca/problem/coci18c3p1

my_string = input().upper()

count = 0
honies = ''

for char in my_string:
    if honies == 'HONI':
        honies = ''

    if honies == '' and char == 'H':
        honies += char
    elif honies == 'H' and char == 'O':
        honies += char
    elif honies == 'HO' and char == 'N':
        honies += char
    elif honies == 'HON' and char == 'I':
        honies += char
        count += 1

print(count)