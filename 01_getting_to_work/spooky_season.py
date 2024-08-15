# Выводить строку "spooky" с количеством букв "o" равным S
# Входные данные: число S, которое 2 <= S <= 20
# Выход: "sp(S*o)ky"

def say_spooky() -> str:
    s = input('Насколько вы ужасны?')
    if not s.isdigit():
        raise ValueError('Not number. Enter number')
    
    s = int(s)
    if s < 2 or s > 20:
        raise ValueError('Expects a value from two to twenty')
    
    oo = ''
    for i in range(s):
        oo += 'o'
    
    spooky = f'sp{oo}ky'
    print(spooky)

say_spooky()