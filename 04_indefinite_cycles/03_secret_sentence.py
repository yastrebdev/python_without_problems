# DMOJ problem - coci08c3p2
# https://dmoj.ca/problem/coci08c3p2

sentence = input()
vowels = 'aeiou'

i = 0

clean_sentence = ''

while i < len(sentence):
    clean_sentence += sentence[i]
    if sentence[i] in vowels:
        i += 3
    else:
        i += 1

print(clean_sentence)