"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from random import randint
from statistics import median

def gnome_sort(lst, size):
    i = 1
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            tmp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = tmp
            i -= 1
            if (i == 0):
                i = 1
    return lst

def median_2(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.

m = int(input('Введите m – натуральное число: '))
lists = [randint(0, 2*m) for i in range(2*m+1)]
newlists = gnome_sort(lists, len(lists))
print(lists)
print(newlists)
print(median(lists))
print(median_2(newlists))