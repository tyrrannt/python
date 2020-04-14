# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools

from itertools import count, cycle


def generate(first):
    for i in count(first, 1):
        yield i


for i in generate(10):
    if i > 150:
        break
    print(i)
