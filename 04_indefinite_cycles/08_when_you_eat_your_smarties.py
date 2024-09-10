# DMOJ problem - ecoo15r1p1
# https://dmoj.ca/problem/ecoo15r1p1

def calculate_time(smarties):
    seconds = 0

    smarties_box = {
        'orange': 0,
        'blue': 0,
        'green': 0,
        'yellow': 0,
        'pink': 0,
        'violet': 0,
        'brown': 0,
    }

    for smartie in smarties:
        if smartie != 'end of box':
            if smartie == 'red':
                seconds += 16
            else:
                smarties_box[smartie] += 1

    for key, value in smarties_box.items():
        remains = smarties_box[key] % 7
        if remains > 0:
            seconds += (int(smarties_box[key] / 7) + 1) * 13
        elif remains == 0:
            seconds += int(smarties_box[key] / 7 * 13)

    return seconds


test_cases = 10
current_case = []

while test_cases > 0:
    smartie = input().strip()
    if smartie == "end of box":
        print(calculate_time(current_case))
        current_case = []
        test_cases -= 1
    else:
        current_case.append(smartie)