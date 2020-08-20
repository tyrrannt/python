"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""


def generate_list(a, b, n):
    from random import randint
    random_list = []
    for i in range(n):
        random_list.append(randint(a, b))
    return random_list


def sort_bubble(lst_obj):
    print(f'Исходный: {lst_obj}')
    for i in range(len(lst_obj) - 1):
        for j in range(len(lst_obj) - i - 1):
            if lst_obj[j] < lst_obj[j + 1]:
                buff = lst_obj[j]
                lst_obj[j] = lst_obj[j + 1]
                lst_obj[j + 1] = buff
    print(f'Отсортированный: {lst_obj}\n')


if __name__ == '__main__':
    from timeit import Timer

    test1 = Timer(lambda: sort_bubble(generate_list(-100, 100, 50)))
    print(f'revers = {test1.timeit(10)}')
