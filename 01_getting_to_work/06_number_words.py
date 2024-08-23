# Подсчитайте количество слов во входных данных.
# Входные данные - это строка, без пробелов в начале и в конце
# Максимальная длина строки — 80 символов.

# my_string = 'problem one is really long'


# def numbers_words(*, string: str) -> int:
#     if len(string) > 80:
#         raise ValueError('Enter no more than 80 characters')
    
#     total_words = string.count(' ') + 1
    
#     return total_words


# print(numbers_words(string=my_string))


def numbers_words() -> int:
    line = input()
    
    if len(line) > 80:
        raise ValueError('Enter no more than 80 characters')
    
    total_words = line.count(' ') + 1
    
    return total_words


print(numbers_words())