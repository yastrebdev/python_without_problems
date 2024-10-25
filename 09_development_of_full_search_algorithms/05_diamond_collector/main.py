# https://usaco.org/index.php?page=viewproblem2&cpid=639

def read_file(file):
    n, k = list(map(int, file.readline().split()))

    diamonds = []
    for i in range(n):
        diamond = int(file.readline())
        diamonds.append(diamond)

    return diamonds, n, k


def max_diamonds_in_display(n, k, diamonds):
    diamonds.sort()

    max_count = 0
    left = 0

    for right in range(n):
        while diamonds[right] - diamonds[left] > k:
            left += 1
        max_count = max(max_count, right - left + 1)

    return max_count


input_file = open('diamond.in', 'r')
output_file = open('diamond.out', 'w')

diamonds, n, k = read_file(input_file)

output_file.write(f'{max_diamonds_in_display(n, k, diamonds)}\n')

input_file.close()
output_file.close()