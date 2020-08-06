"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import random


def benchmark(func):
    import time

    def wrapper(args):
        start = time.time()
        result = func(args)
        end = time.time()
        print(f'[*] Время выполнения: {end - start} секунд.')
        return result

    return wrapper


@benchmark
def list_obj(elements):
    origin_list = []
    for i in range(0, elements):
        origin_list.append(i ** elements)
    return origin_list


@benchmark
def dict_obj(elements):
    origin_dict = {}
    for i in range(0, elements):
        origin_dict[i] = ( i ** elements)
    return origin_dict


count = int(input('Введите количество элементов'))
result = list_obj(count)
result = dict_obj(count)