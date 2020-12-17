# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = []
while True:
    new_item = input(f"Введите значение элемента, или нажмите кнопку Enter для завершения ввода = ")
    if new_item != "":
        my_list.append(new_item)
    else:
        break
print("Список = ", my_list)
i = 0
while i < len(my_list)-1:
    first_var, second_var = my_list[i], my_list[i+1]
    my_list[i + 1], my_list[i] = first_var, second_var
    i += 2
print("Список = ", my_list)
