# Вычислите объем правильного конуса
# Входные данные:
# r - радиус конуса
# h - высота конуса
# значения r и h находятся в диапазоне от 1 до 100
# Выводится объем правильного конуса
# Формула для расчета - PI*r*2h/3

PI = 3.141592653589793


def my_input(message: str) -> int:
    value = input(message)
    if not value.isdigit():
        raise ValueError('Enter an integer or a number with a dot')
    
    value = int(value)
    if value < 1 or value > 100:
        raise ValueError('Enter a number from 1 to 100')
    return value


def cone_volume() -> float:
    radius = int(my_input("Введите радиус конуса:"))
    height = int(my_input("Введите высоту конуса:"))
    
    volume = (PI * radius ** 2 * height) / 3
    
    return volume


print(cone_volume())