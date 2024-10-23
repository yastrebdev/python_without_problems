# DMOJ problem - ccc06s2
# https://dmoj.ca/problem/ccc06s2

def read_messages():
    open_message = input().upper()
    close_message = input().upper()

    comparison = {}
    for i in range(len(open_message)):
        if close_message[i] in comparison:
            continue
        else:
            comparison[close_message[i]] = open_message[i]

    encrypted_message = input().upper()

    return comparison, encrypted_message


def decoding(message):
    decrypted_message = ''
    for char in message:
        if char in comparison:
            decrypted_message += comparison[char]
        else:
            decrypted_message += '.'

    return decrypted_message


comparison, encrypted_message = read_messages()
decrypted_message = decoding(encrypted_message)

print(decrypted_message)