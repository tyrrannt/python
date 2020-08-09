"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from random import randint
array = [1, 3, 1, 3, 4, 5, 1]
array = [i*randint(1, 100) for i in range(50)]

def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

# Прям быстрее не получается, но результат лучше чем дает вторая функция
def func_3():
    max_3 = 0
    for i in array:
        if max_3 < array.count(i):
            max_3 = array.count(i)
            elem = i
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


if __name__ == '__main__':
    from timeit import Timer
    print(func_1())
    print(func_2())
    print(func_3())

    test1 = Timer(lambda: func_1())
    test2 = Timer(lambda: func_2())
    test3 = Timer(lambda: func_3())

    print(test1.timeit(10000))
    print(test2.timeit(10000))
    print(test3.timeit(10000))

