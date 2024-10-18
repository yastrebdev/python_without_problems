# DMOJ problem - ecoo19r2p1
# https://dmoj.ca/problem/ecoo19r2p1

def clean_email(address: str) -> str:
    """
    address - это адрес электронной почты.

    Возвращает очищенный адрес.
    """

    plus_index = address.find('+')
    if plus_index != -1:
        at_index = address.find('@')
        address = address[:plus_index] + address[at_index:]

    at_index = address.find('@')
    before_at = ''
    i = 0
    while i < at_index:
        if address[i] != '.':
            before_at += address[i]
        i += 1

    cleaned = before_at + address[at_index:]

    cleaned = cleaned.lower()

    return cleaned


for dataset in range(10):
    n = int(input())
    addresses = set()
    for _ in range(n):
        address = input()
        address = clean_email(address)
        addresses.add(address)

    print(len(addresses))