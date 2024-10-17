# https://usaco.org/index.php?page=viewproblem2&cpid=963

def write_workout(file, k):
    workouts = []
    for _ in range(k):
        workout = list(map(int, file.readline().split()))
        workouts.append(workout)

    return workouts


def counting_pairs(workouts):
    pairs = []
    for w in workouts:
        for i in range(len(w)):
            for j in range(i+1, len(w)):
                pairs.append([w[i], w[j]])

    return pairs


def filter_nested_lists(lst, min_count):
    tuple_list = [tuple(sublist) for sublist in lst]

    element_counts = {}
    for elem in tuple_list:
        if elem in element_counts:
            element_counts[elem] += 1
        else:
            element_counts[elem] = 1

    filtered_tuples = [elem for elem in tuple_list if element_counts[elem] >= min_count]

    filtered_lists = [list(sublist) for sublist in filtered_tuples]
    unique_list = list(map(list, set(map(tuple, filtered_lists))))

    return len(unique_list)


input_file = open('gymnastics.in', 'r')
output_file = open('gymnastics.out', 'w')

k, n = list(map(int, input_file.readline().split()))
workouts = write_workout(input_file, k)
pairs = counting_pairs(workouts)
count = filter_nested_lists(pairs, k)
output_file.write(str(count))

input_file.close()
output_file.close()