# DMOJ problem - ccc07j3
# https://dmoj.ca/problem/ccc07j3

briefcases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]


def making_deal():
    exceptions = int(input())
    for _ in range(exceptions):
        n = int(input())
        briefcases[n - 1] = 0

    deal = int(input())

    average = sum(briefcases) / (len(briefcases) - exceptions)
    print(average)
    print(briefcases)

    if deal > average:
        return 'deal'
    else: return  'no deal'


print(making_deal())