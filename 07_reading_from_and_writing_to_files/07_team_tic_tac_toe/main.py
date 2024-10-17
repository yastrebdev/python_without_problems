# https://usaco.org/index.php?page=viewproblem2&cpid=831


def reed_board(file):
    board = []

    for i in range(3):
        line = file.readline().strip()
        row = []
        for char in line:
            row.append(char)
        board.append(row)

    return board


def determine_winners(board):
    winners = [0, 0]

    sequences = [
        board[0],
        board[1],
        board[2],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]]
    ]

    for seq in sequences:
        if seq.count(seq[0]) == 2:
            winners[1] += 1
        elif seq.count(seq[0]) == 3:
            winners[0] += 1

    return winners


def write_score(winners, file):
    for win in winners:
        file.write(f'{str(win)}\n')


input_file = open('tttt.in', 'r')
output_file = open('tttt.out', 'w')

board = reed_board(input_file)
winners = determine_winners(board)
write_score(winners, output_file)

input_file.close()
output_file.close()