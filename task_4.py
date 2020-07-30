"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
from random import randrange

def number_sign(num):
    if num % 2 == 0:
        return 2 ** num
    else:
        return - (2 ** num)


def number_of_shifter(num, count):
    if count == 1:
        return num[0]
    else:
        return num[0] + number_of_shifter(num[1:], count - 1)


steps = int(input('Введите количество элементов: '))
row_numbers = [1 / number_sign(i) for i in range(0, steps)]
print(row_numbers)
print(number_of_shifter(row_numbers, steps))
