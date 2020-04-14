# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools

from itertools import count, cycle, islice


def generate(first, step=1):
    """
    Генерация целых чисел
    :param first: с какого числа начать
    :param step: шаг, опциональный аргумент, по умолчании 1
    :return:
    возвращает бесконечный итератор
    """
    for i in count(first, 1):
        yield i


my_list = []

for i in generate(70):
    if i > 80:
        break
    # Новый список заполняется символами по их числовому представлению
    my_list.append(chr(i))

print(my_list)
for i in islice(cycle(my_list), 12):
    print(i)
