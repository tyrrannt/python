# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(first, second, third):
    """
    Функция возвращает сумму наибольших двух аргументов

    :param first: Первый аргумент
    :param second: Второй аргумент
    :param third: Третий аргумент
    :return: Возвращает сумму наибольших двух аргументов
    """
    return second + third if second > first < third else (first + third if first > second < third else first + second)

while True:
    a = int(input("Введите первую переменную: "))
    b = int(input("Введите вторую переменную: "))
    c = int(input("Введите третью переменную: "))
    print(my_func(a, b, c))
