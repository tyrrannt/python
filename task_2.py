"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
from random import randint

source_list = [randint(0, 1000) for i in range(0, 100)]

# O(n**2)
def quadratic_complexity(source):
    minimum = source[0]
    for first in source:
        for second in source:
            if first < second:
                middle = first
            else:
                middle = second
        if minimum > middle:
            minimum = middle
    return minimum

# O(n)
def linear_complexity(source):
    minimum = source[0]
    for item in source:
        if item < minimum:
            minimum = item
    return minimum


print(source_list)
print(quadratic_complexity(source_list))
print(linear_complexity(source_list))
