# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider, rounding=3):
    """
    Функция деления двух чисел.

    :param dividend: Параметр в который передается "Делимое", допустимый тип данных int, float.
    :param divider: Параметр в который передается "Делитель", допустимый тип данных int, float.
    :param rounding: Необязательный параметр. Округление числа после запятой. По умолчанию 3, допустимый тип данных int.
    :return: В случае ввода корректных данных возвращает результат деления тип float.
    """
    return round(dividend / divider, rounding)


try:
    first_arg = int(input("Введите делимое: "))
    second_arg = int(input("Введите делитель: "))
    print(f"{first_arg}/{second_arg} =", division(first_arg, second_arg, 10))
except Exception as error:
    print(error)
