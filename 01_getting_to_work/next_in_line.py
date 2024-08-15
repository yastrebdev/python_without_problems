# Мы знаем семью с тремя детьми.
# Их возраст образует арифметическую последовательность:
# разница в возрасте между средним ребенком и младшим ребенком такая же,
# как разница в возрасте между старшим ребенком и средним ребенком.
# Учитывая возраст младших и средних детей, каков возраст старшего ребенка?
# Вход: y (0 <= y <= 50) - x (0 <= x <= 50)
# Возраст самого старшего ребенка - int


def my_input(message: str) -> str:
    value = input(message)
    if not value.isdigit():
        raise ValueError('Enter an integer or a number with a dot')
    value = int(value)
    if value < 1 or value > 50:
        raise ValueError('Enter a number from 1 to 100')
    return value


def calculate_the_age_of_the_eldest_child():
    y = my_input('Возраст младшего ребенка')
    x = my_input('Возраст среднего ребенка')
    
    age_of_the_eldest_child = 2*x - y
    return age_of_the_eldest_child

age = calculate_the_age_of_the_eldest_child()

print(age)