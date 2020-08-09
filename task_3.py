"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

if __name__ == '__main__':
    from timeit import Timer
    test1 = Timer(lambda: revers(65498732110646548))
    test2 = Timer(lambda: revers_2(65498732110646548))
    test3 = Timer(lambda: revers_3(65498732110646548))
    print(f'revers = {test1.timeit(100000)}; revers_2 = {test2.timeit(100000)}; revers_3 = {test3.timeit(100000)}')