# DMOJ problem - ccc11s2
# https://dmoj.ca/problem/ccc11s2

n = int(input())

answers = ''
true_answers = ''

count = 0

for i in range(n):
    a = input()
    answers += a

for i in range(n):
    ta = input()
    true_answers += ta

for i in range(n):
    if answers[i] == true_answers[i]:
        count += 1

print(count)