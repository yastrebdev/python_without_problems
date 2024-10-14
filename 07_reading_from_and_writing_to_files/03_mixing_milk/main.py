# https://usaco.org/index.php?page=viewproblem2&cpid=855

def get_buckets(file):
    buckets = []
    for _ in range(3):
        volumes = list(map(int, file.readline().split()))
        buckets.append(volumes)

    return buckets


def pour_over_milk(buckets):
    for i in range(1, 101):
        buck_num = i % 3
        prev_buck_num = (i - 1) % 3

        volume = buckets[prev_buck_num][1] + buckets[buck_num][1]

        if volume > buckets[buck_num][0]:
            buckets[buck_num][1] = buckets[buck_num][0]
            buckets[prev_buck_num][1] = volume - buckets[buck_num][1]
        else:
            buckets[buck_num][1] = volume
            buckets[prev_buck_num][1] = 0

    volumes = [bucket[1] for bucket in buckets]

    return volumes


def write_result(file, volumes):
    for vol in volumes:
        file.write(str(vol) + '\n')


input_file = open('mixmilk.in', 'r')
output_file = open('mixmilk.out', 'w')

buckets = get_buckets(input_file)

result_volumes = pour_over_milk(buckets)

write_result(output_file, result_volumes)

input_file.close()
output_file.close()