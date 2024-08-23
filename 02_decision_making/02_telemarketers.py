# Существует некоторая последовательность, по которой можно определить
# номер телемаркетолога:
# первая цифра 8 или 9
# четвертая цифра 8 или 9
# вторая и третья цифры совпадают
# Задача: определить принадлежит ли номер телемаркетологу.
# Ввод: 4 строки, в которых указаны цифры от 0 до 9
# Вывод: Если телефон принадлежит телемаркетологу, то ignore, если нет, то answer

one = int(input('One: '))
two = int(input('Two: '))
three = int(input('Three: '))
four = int(input('Four: '))

if ((one == 8 or one == 9) and
    (four == 8 or four == 9) and
    (two == three)):
    print('ignore')
else:
    print('answer')