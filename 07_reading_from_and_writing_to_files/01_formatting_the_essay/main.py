input_file = open('word.in', 'r')
output_file = open('word.out', 'w')

n, k = list(map(int, input_file.readline().split()))
words = input_file.readline().split()

line = ''
chars_on_line = 0

for word in words:
    if chars_on_line + len(word) <= k:
        line += word + ' '
        chars_on_line += len(word)
    else:
        output_file.write(line[:-1] + '\n')
        line = word + ' '
        chars_on_line = len(word)

output_file.write(line[:-1] + '\n')

input_file.close()
output_file.close()