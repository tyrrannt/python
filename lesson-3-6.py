# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(my_str, variable=1):
    """
    Функция преобразовани слова.

    :param my_str: Содержит переданное слово
    :param variable: Вариант использования. 0 - при помощи capitalize, 1 - при помощи upper и lower
    :return: Возвращает слово в нижнем регистре с заглавной буквой.
    """
    if variable != 1:
        return my_str.capitalize()
    else:
        result = my_str[0].upper() + my_str[1:].lower()
        return result


def int_long_func(my_str, variable=1):
    """
    Функция преобразовани строки.

    :param my_str: Содержит переданную строку
    :param variable: Вариант использования. 0 - при помощи capitalize, 1 - при помощи upper и lower
    :return: Возвращает строку в нижнем регистре с заглавной буквой у каждого слова.
    """
    result = []
    middle = my_str.split(' ')
    for arg in middle:
        result.append(int_func(arg, variable))
    return (' ').join(result)


my_str = input("Введите строку или слово: ")
my_list = my_str.split(' ')
if len(my_list) == 1:
    print(int_func(my_str))
else:
    print(int_long_func(my_str))
