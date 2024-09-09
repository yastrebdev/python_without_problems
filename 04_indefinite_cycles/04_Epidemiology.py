# DMOJ problem - ccc20j2
# https://dmoj.ca/problem/ccc20j2

target = int(input())
sick = int(input())
get_sick = int(input())

new_sick = 0
total_sick = sick
day = 0

while total_sick <= target:
    if day == 0:
        new_sick += get_sick * sick
    else:
        new_sick *= get_sick

    total_sick += new_sick
    day += 1

print(day)