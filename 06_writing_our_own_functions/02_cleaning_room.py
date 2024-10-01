# https://acm.timus.ru/problem.aspx?space=1&num=2144

# Основная программа
# TODO: Чтение входных данных
# TODO: Проверка корректности всех коробок
# TODO: Получение нового списка коробок, в которых
    # остаются только крайние фигурки
# TODO: Сортировка коробок
# TODO: Определение того, организованы ли коробки

count_boxes = int(input())

def read_boxes(n):
    bxs = []
    for i in range(n):
        box = list(map(int, input().split()[1:]))
        bxs.append(box)
    return bxs


def is_order_in_boxes(bxs):
    for box in bxs:
        prev_fh = 0
        for fh in box:
            if fh >= prev_fh:
                prev_fh = fh
            else: return False
    return True


def new_boxes(bxs):
    new_bxs = []
    for box in bxs:
        new_bxs.append([box[0], box[-1]])

    return new_bxs


def main(n):
    boxes = read_boxes(n)
    if is_order_in_boxes(boxes):
        boxes = new_boxes(boxes)
    else: return 'NO'

    boxes.sort()

    prev_last_fh = 0
    for box in boxes:
        first_fh = box[0]
        if first_fh > prev_last_fh:
            prev_last_fh = box[1]
        else:
            return 'NO'

    return  'YES'


print(main(count_boxes))