# DMOJ problem - ccc02j2
# https://dmoj.ca/problem/ccc02j2

translate_list = []
vowel = 'aeiouy'
word = ''

while word != 'quit!':
    word = input()
    if word != 'quit!':
        if len(word) > 4 and word[-2:] == 'or' and word[-3] not in vowel:
            translate = word[:-1] + 'ur'
            translate_list.append(translate)
        else:
            translate_list.append(word)

for word in translate_list:
    print(word)