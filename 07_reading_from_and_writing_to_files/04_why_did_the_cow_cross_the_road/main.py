# https://usaco.org/index.php?page=viewproblem2&cpid=720

def read_fields(file):
    num_breeds = int(file.readline())
    fields = []

    for _ in range(2):
        side = []
        for _ in range(num_breeds):
            side.append(int(file.readline()))
        fields.append(side)

    return fields

def find_intersections(left_side, right_side):
    num_fields = len(left_side)
    intersections = 0

    right_indices = {right_side[i]: i for i in range(num_fields)}

    for i in range(num_fields):
        for j in range(i + 1, num_fields):
            left_cow_a = left_side[i]
            left_cow_b = left_side[j]

            right_cow_a = right_indices[left_cow_a]
            right_cow_b = right_indices[left_cow_b]

            if right_cow_a > right_cow_b:
                intersections += 1

    return intersections

def cyclic_shift(left_side, right_side):
    intersections_list = []
    n = len(right_side)

    for k in range(n):
        new_order = right_side[k:] + right_side[:k]

        intersections = find_intersections(left_side, new_order)
        intersections_list.append(intersections)

    return min(intersections_list)


def write_intersections(intersections):
    output_file.write(str(intersections) + "\n")


input_file = open('mincross.in', 'r')
output_file = open('mincross.out', 'w')

left_side, right_side = read_fields(input_file)
min_intersections = cyclic_shift(left_side, right_side)
write_intersections(min_intersections)

input_file.close()
output_file.close()