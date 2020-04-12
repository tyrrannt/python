# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools

from itertools import count, cycle

first_step = round(1000)
def generate(first):

    yield count(first, 1)

print(first_step)
i = 1
while i < 100:
    print(generate(first_step))
    print(cycle(generate(first_step)))
    i +=1


