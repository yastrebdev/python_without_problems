def search_cow(x, y):
    distance = 0
    step_size = 1
    current_pos = x
    next_pos = x + step_size
    direction = 1

    while True:
        if (current_pos <= y <= next_pos) or (current_pos >= y >= next_pos):
            distance += abs(y - current_pos)
            break
        else:
            distance += abs(next_pos - current_pos)
            current_pos = next_pos
            step_size *= 2
            direction *= -1
            next_pos = x + direction * step_size

    return distance


input_file = open('lostcow.in', 'r')
output_file = open('lostcow.out', 'w')

x, y = list(map(int, input_file.readline().split()))

distance = search_cow(x, y)
output_file.write(str(distance))

input_file.close()
output_file.close()