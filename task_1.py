"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# Выполнил в виде генератора списка, почти в 2 раза быстрее
def func_2(nums):
    return [i for i in nums if i % 2 == 0]



if __name__ == '__main__':
    from timeit import Timer

    array = [i for i in range(300)]
    test1 = Timer(lambda: func_1(array))
    test2 = Timer(lambda: func_2(array))
    print(test1.timeit(50000))
    print(test2.timeit(90000))
