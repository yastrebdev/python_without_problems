# DMOJ problem - coci17c2p2
# https://dmoj.ca/problem/coci17c2p2

def read_words():
    w, l = list(map(int, input().split()))

    words = {}
    indexes = {}
    for _ in range(w):
        word = input().strip()
        if word[0] in words:
            words[word[0]].append(word)
        else:
            words[word[0]] = [word]
            indexes[word[0]] = 0

    for key in words:
        words[key].sort()

    letters = []
    for _ in range(l):
        letter = input().strip()
        letters.append(letter)

    return words, indexes, letters


words, indexes, letters = read_words()

output_words = []
for letter in letters:
    index = indexes[letter]
    word = words[letter][index]
    output_words.append(word)

    if index == len(words[letter]) - 1:
        indexes[letter] = 0
    else:
        indexes[letter] += 1

for ow in output_words:
    print(ow)