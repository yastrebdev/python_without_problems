# https://usaco.org/index.php?page=viewproblem2&cpid=866

def read_cows(input_file, num_cows):
    """
    input_file — это открытый для чтения файл
    с информацией о коровах.

    num_cows — это количество коров в файле.

    Требуется прочитать число коров из файла
    и информацию о них.
    Возвращает список двух любимых пастбищ коровы.
    """
    favorites = []
    for _ in range(num_cows):
        lst = list(map(int, input_file.readline().split()))
        favorites.append(lst)

    return favorites


def cows_with_favorite(favorites, pasture):
    """
    favorites — это список любимых пастбищ, получаемый
    из функции read_cows.

    pasture — это номер пастбища.

    Возвращает список коров, которые любят это пастбище.
    """
    cows = []
    for i in range(len(favorites)):
        if favorites[i][0] == pasture or favorites[i][1] == pasture:
            cows.append(i)

    return cows


def types_used(favorites, cows, pasture_types):
    """
    favorites — это список любимых пастбищ, получаемый
    из функции read_cows.

    cows — это список коров.

    pasture_types — это список типов травы.

    Возвращает список типов травы, уже "занятых" коровами.
    """
    used = []
    for cow in cows:
        pasture_a = favorites[cow][0]
        pasture_b = favorites[cow][1]
        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a])
        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b])

    return used


def smallest_available(used):
    '''
    used — это список использованных типов травы.

    Возвращает наименьший номер еще не тронутой травы.
    '''
    grass_type = 1
    while grass_type in used:
        grass_type += 1

    return grass_type


def write_pastures(output_file, pasture_types):
    '''
    output_file — это файл, в который будет записан результат.
    pasture_types — это список типов травы

    Функция выводит pasture_types в output_file.
    '''
    pasture_types_str = []
    for pasture_type in pasture_types:
        pasture_types_str.append(str(pasture_type))
    output = ''.join(pasture_types_str)
    output_file.write(output + '\n')


input_file = open('revegetate.in', 'r')
output_file = open('revegetate.out', 'w')

num_pastures, num_cows = list(map(int, input_file.readline().split()))
favorites = read_cows(input_file, num_cows)

pasture_types = [0]

for i in range(1, num_pastures + 1):
    cows = cows_with_favorite(favorites, i)
    eliminated = types_used(favorites, cows, pasture_types)
    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_type)

pasture_types.pop(0)
write_pastures(output_file, pasture_types)

input_file.close()
output_file.close()