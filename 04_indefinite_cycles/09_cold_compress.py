# DMOJ problem - ccc19j3
# https://dmoj.ca/problem/ccc19j3

str_count = int(input())

message = []
for i in range(str_count):
    my_str = input()

    line_coding = ''
    sequence = ''
    for index, char in enumerate(my_str):
        if index == 0:
            sequence += char
            continue

        if sequence[0] == char:
            sequence += char
            if index == len(my_str) - 1:
                line_coding += f'{len(sequence)} {sequence[0]} '
        else:
            line_coding += f'{len(sequence)} {sequence[0]} '
            sequence = char
            if index == len(my_str) - 1:
                line_coding += f'{len(sequence)} {sequence[0]} '

    message.append(line_coding)

for i in range(len(message)):
    print(message[i].strip())



# def compress_string(s):
#     compressed = []
#     count = 1
#
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             compressed.append(f"{count} {s[i - 1]}")
#             count = 1
#     compressed.append(f"{count} {s[-1]}")
#     return " ".join(compressed)
#
# n = int(input())
# for _ in range(n):
#     line = input().strip()
#     print(compress_string(line))