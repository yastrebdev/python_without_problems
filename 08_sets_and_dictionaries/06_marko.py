# DMOJ problem - coci15c2p1
# https://dmoj.ca/problem/coci15c2p1

def read_inputs():
    n = int(input())

    dictionary = set()
    for _ in range(n):
        dictionary.add(input())

    sequence = input()

    return dictionary, sequence


def corresponds_sequence(word, kb, seq):
    sequence = ''
    for char in word:
        for key in kb.keys():
            if char in key:
                sequence += kb[key]
                break

    if sequence == seq[:len(sequence)]:
        return True
    else:
        return False


keyboard = {
    'abc': '2',
    'def': '3',
    'ghi': '4',
    'jkl': '5',
    'mno': '6',
    'pqrs': '7',
    'tuv': '8',
    'wxyz': '9',
}

dictionary, sequence = read_inputs()

count_words = 0
for word in dictionary:
    if corresponds_sequence(word, keyboard, sequence):
        count_words += 1

print(count_words)