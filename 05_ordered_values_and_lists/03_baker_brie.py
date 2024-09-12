# DMOJ problem - ecoo17r3p1
# https://dmoj.ca/problem/ecoo17r3p1

def calculate_bonus() -> int:
    bonuses = 0
    all_sales = []

    fd: list = input().split()

    sales = []
    for d in range(int(fd[1])):
        sales_for_day: list = input().split()
        for f in range(int(fd[0])):
            sales_for_day[f] = int(sales_for_day[f])

            if d == 0:
                all_sales.append(sales_for_day[f])
            else:
                all_sales[f] += sales_for_day[f]

        sales.append(sales_for_day)

        if sum(sales_for_day) % 13 == 0:
            bonuses += sum(sales_for_day) / 13

    for sd in all_sales:
        if sd % 13 == 0:
            bonuses += sd / 13

    return int(bonuses)


for _ in range(10):
    print(calculate_bonus())