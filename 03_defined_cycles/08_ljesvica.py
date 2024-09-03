# DMOJ problem - coci12c5p1
# https://dmoj.ca/problem/ccc11s2

# Моё решение
# sequence = input()
#
# minor_tone = ['A', 'D', 'E']
# major_tone = ['C', 'F', 'G']
#
# melody = sequence.split('|')
#
# tonality_A = ''
# tonality_C = ''
#
# for tact in melody:
#     first_char = tact[0]
#
#     if first_char in minor_tone:
#         tonality_A += first_char
#     elif first_char in major_tone:
#         tonality_C += first_char
#     else: continue
#
# last_note = melody[-1]
#
# if len(tonality_A) > len(tonality_C) or len(tonality_A) == len(tonality_C) and last_note == 'A':
#     print('A-mol')
# elif len(tonality_C) > len(tonality_A) or len(tonality_A) == len(tonality_C) and last_note == 'C':
#     print('C-dur')


# Решение ChatGPT
melody = input()

a_minor_main_tones = {'A', 'D', 'E'}
c_major_main_tones = {'C', 'F', 'G'}

measures = melody.split('|')
accented_tones = [measure[0] for measure in measures]

a_minor_count = sum(1 for tone in accented_tones if tone in a_minor_main_tones)
c_major_count = sum(1 for tone in accented_tones if tone in c_major_main_tones)

if a_minor_count > c_major_count:
    print('A-mol')
elif c_major_count > a_minor_count:
    print('C-dur')
else:
    print('A-mol') if melody[-1] == 'A' else print('C-dur')