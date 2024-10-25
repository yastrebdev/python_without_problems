# https://usaco.org/index.php?page=viewproblem2&cpid=891

def read_data_games(file):
    n = int(file.readline())

    moves = {}
    trying = []
    for i in range(n):
        game = list(map(int, file.readline().split()))

        moves[i + 1] = set(game[0:2])
        trying.append(game[2])

    return moves, trying, n


input_file = open('shell.in', 'r')
output_file = open('shell.out', 'w')

moves, trying, n = read_data_games(input_file)

total = 0
for i in range(1, n + 1):
    points = 0
    current_position = i
    for j in range(1, n + 1):
        move = moves[j]
        one_try = trying[j - 1]
        if current_position in move:
            new_position = move - {current_position}
            current_position = new_position.pop()

        if current_position == one_try:
            points += 1

    if points > total:
        total = points

output_file.write(f'{total}\n')

input_file.close()
output_file.close()