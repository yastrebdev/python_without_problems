# DMOJ problem - wc17c3j3
# https://dmoj.ca/problem/wc17c3j3

password = input()

lower = ''
upper = ''
number = ''
other = ''

if 8 <= len(password) <= 12:
    for char in password:
        if char.islower():
            lower += char
        elif char.isupper():
            upper += char
        elif char.isdigit():
            number += char
        else:
            other += char

    if len(lower) < 3 or len(upper) < 2 or len(number) < 1 or len(other) > 0:
        print('Invalid')
    else: print('Valid')
else: print('Invalid')