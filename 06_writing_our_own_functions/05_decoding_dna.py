# DMOJ problem - ecoo12r1p2
# https://dmoj.ca/problem/ecoo12r1p2

def comp_sequence(substring, marker='seq'):
    comp_ss = ''
    for char in substring:
        if char == 'A':
            if marker == 'rna':
                comp_ss += 'U'
            else:
                comp_ss += 'T'
        elif char == 'T':
            comp_ss += 'A'
        elif char == 'G':
            comp_ss += 'C'
        elif char == 'C':
            comp_ss += 'G'

    return comp_ss


def search_terminator(sequence):
    trs = None
    min_lt = 6

    for i in range(len(sequence)):
        if trs:
            break
        one_term = sequence[i:min_lt + i]
        for j in range(len(sequence) - min_lt):
            two_term = sequence[min_lt + j:min_lt * 2 + j]
            comp_ss = comp_sequence(two_term)
            reverse_ss = comp_ss[::-1]
            if one_term == reverse_ss:
                index = sequence.find(one_term)
                trs = sequence[:index]
                break

    return trs


def calculate_rna(sequence):
    promoter = 'TATAAT'
    lp = len(promoter)

    for i in range(len(sequence)):
        if sequence[i:lp + i] == promoter:
            sequence = sequence[lp + i + 4:]
            break

    trs = search_terminator(sequence)
    comp_ss = comp_sequence(trs, 'rna')
    return comp_ss


for s in range(1, 6):
    dna = input().upper()
    rna = calculate_rna(dna)
    print(f'{s}: {rna}')