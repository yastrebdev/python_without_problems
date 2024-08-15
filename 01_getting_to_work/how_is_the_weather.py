# Написать функцию, которая конверстирует цельсии в фаренгейты
# Ввод: -40 <= c <= 40
# Вывод: int

def celsius_to_fahrenheit() -> int:
    c = input('Введите градусы')
    if not c.isdigit:
        raise ValueError('Enter an integer or a number with a dot')
    c = int(c)
    if c < -40 or c > 40:
        raise ValueError('Enter a number from -40 to 40')

    f = int(1.8 * c + 32)
    
    return f

print(celsius_to_fahrenheit())