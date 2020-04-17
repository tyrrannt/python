# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
from functools import reduce


def num_list(x, y):
    return int(x) + int(y)


with open(r"my_text_2.txt", "w") as file_d:
    for i in range(1, 1000):
        file_d.write(f"{randint(1, i)} ")

my_list = []
with open(r"my_text_2.txt", "r") as file_d:
    for i in file_d:
        my_list = i.split(' ')
        print(my_list)
        print(reduce(num_list, my_list[:-1]))
