# https://usaco.org/index.php?page=viewproblem2&cpid=376

MAX_DIFFERENCE = 17
MAX_HEIGHT = 100

def cost_for_range(heights, low, high):
    """
    :param heights: это список высот холмов
    :param low: это нижняя граница диапазона высот
    :param high: это верхняя граница диапазона высот
    :return: стоимость приведения высот всех холмов в заданный диапазон
    """

    cost = 0
    for height in heights:
        if height < low:
            cost += (low - height) ** 2
        elif height > high:
            cost += (height - high) ** 2

    return cost


input_file = open('skidesign.in', 'r')
output_file = open('skidesign.out', 'w')

n = int(input_file.readline())

heights = [int(input_file.readline()) for _ in range(n)]

min_cost = cost_for_range(heights, 0, MAX_DIFFERENCE)

for low in range(1, MAX_HEIGHT + 1):
    result = cost_for_range(heights, low, low + MAX_DIFFERENCE)
    if result < min_cost:
        min_cost = result

output_file.write(str(min_cost) + '\n')

input_file.close()
output_file.close()