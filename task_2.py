"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""


def memoize(func):
    cache = {}

    def decor(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]

    return decor


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


if __name__ == '__main__':
    from timeit import Timer

    test1 = Timer(lambda: recursive_reverse(65498732110646548))
    test2 = Timer(lambda: recursive_reverse_mem(65498732110646548))
    print(
        f'С мемоизацией 10 000 000 запусков = {test2.timeit(number=10000000)}. \nБез мемоизации  330 000  запусков = {test1.timeit(number=330000)}')
