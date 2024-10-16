def write_workout(file):
    k, n = list(map(int, file.readline().split()))

    workouts = []
    for _ in range(k):
        workout = list(map(int, file.readline().split()))
        workouts.append(workout)

    return workouts


def counting_pairs(workouts):
    permanent_pairs = 0


    for w in workouts:
        for i in range(len(w)):
            for j in range(i+1, len(w)):
                pass

    return permanent_pairs


input_file = open('gymnastics.in', 'r')
output_file = open('gymnastics.out', 'w')

workouts = write_workout(input_file)
permanent_pairs = counting_pairs(workouts)

input_file.close()
output_file.close()