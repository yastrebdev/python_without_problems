# Добавить N "far" в строку с запятой после каждого "far", кроме последнего
# Входные данные: число N, которое 1 <= S <= 5
# Примерный ыход: "A long time ago in a galaxy far, far, far, far away..."

# def how_far() -> str:
#     n = input('Ну и как далеко?')
#     if not n.isdigit():
#         raise ValueError('Not number. Enter number')
    
#     n = int(n)
#     if n < 1 or n > 5:
#         raise ValueError('Expects a value from two to five')
    
#     far = ''
#     for i in range(n):
#         if n - 1 == i:
#             far += 'far'
#         else:
#             far += 'far, '
    
#     string = f'A long time ago in a galaxy {far} away...'
#     print(string)

# how_far()

def generate_sentence():
    n = int(input('Ну и как далеко?'))
    if n < 1 or n > 5:
        raise ValueError('Expects a value from two to five')
    far_sequence = ", ".join(["far"] * n)
    
    sentence = f"A long time ago in a galaxy {far_sequence} away..."
    
    return sentence

print(generate_sentence())