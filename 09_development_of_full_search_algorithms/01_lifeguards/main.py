# https://usaco.org/index.php?page=viewproblem2&cpid=792

def num_covered(intervals, fired):
    """
    :param intervals: список интервалов работы спасателя
        каждый интервал представляет собой список вида [start, end]
    :param fired: это индекс увольняемого спасателя
    :return: число интервалов времени, охваченных спасателями, не считая уволенного.
    """

    covered = set()

    for i in range(len(intervals)):
        if i != fired:
            interval = intervals[i]
            for j in range(interval[0], interval[1]):
                covered.add(j)

    return len(covered)


input_file = open('lifeguards.in', 'r')
output_file = open('lifeguards.out', 'w')

n = int(input_file.readline())

intervals = []

for i in range(n):
    interval = list(map(int, input_file.readline().split()))
    intervals.append(interval)

max_covered = 0

for fired in range(n):
    result = num_covered(intervals, fired)
    if result > max_covered:
        max_covered = result

output_file.write(str(max_covered) + '\n')

input_file.close()
output_file.close()