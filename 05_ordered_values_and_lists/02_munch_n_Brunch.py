# DMOJ problem - ecoo17r1p1
# https://dmoj.ca/problem/ecoo17r1p1

COSTS = [12, 10, 7, 5]


def calculate_money():
    cost = int(input())
    students_percent: list = input().split()
    students_at_breakfast = int(input())

    for i in range(len(students_percent)):
        students_percent[i] = float(students_percent[i])

    students_each_course = []
    for value in students_percent:
        students_each_course.append(int(value * students_at_breakfast))

    if sum(students_each_course) < students_at_breakfast:
        difference = students_at_breakfast - sum(students_each_course)
        max_course = max(students_each_course)
        index_mc = students_each_course.index(max_course)
        students_each_course[index_mc] += difference

    money_each_course = []
    for i, c in enumerate(COSTS):
        money_each_course.append(students_each_course[i] * c)

    result = sum(money_each_course) / 2

    if result >= cost:
        return 'NO'
    else: return 'YES'


for _ in range(10):
    print(calculate_money())