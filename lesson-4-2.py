# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

from random import randrange

my_list = [randrange(i) for i in range(1, 40)]
print(my_list)
i = 1
result = []
while i < len(my_list):
    if my_list[i] > my_list[i - 1]:
        result.append(my_list[i])
    i += 1
print(result)
