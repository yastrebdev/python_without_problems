# DMOJ problem - coci13c3p1
# https://dmoj.ca/problem/coci13c3p1

taps = int(input())

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1

    num = fibonacci(n - 1) + fibonacci(n - 2)

    return num

print(f'{fibonacci(taps - 1)} {fibonacci(taps)}')