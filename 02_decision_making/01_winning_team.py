# Играют две баскетбольные команды
# Каждая команда за игру забивает трёх-очковые, двух-очковые и штрафные мячи
# Задача: Посчитать количество заработанных очков у каждой команды
# и вывести в консоль:
# букву A, если победила первая команда;
# букву B, если победила вторая команда;
# букву T, если ничья.
# Вход: n, n, n, n, n, n. Где n целое натуральное число
# Выход: A or D or T

la = int(input())
ma = int(input())
sa = int(input())

lb = int(input())
mb = int(input())
sb = int(input())

da = la*  3 + ma * 2 + sa
db = lb*  3 + mb * 2 + sb

if da > db:
    print('A')
elif db > da:
    print('B')
else:
    print('T')