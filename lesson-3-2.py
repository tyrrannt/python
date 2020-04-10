# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def personal_data(**kwargs):
    """
    Функция для вывода данных пользователя

    :param kwargs: Принимает именованные аргументы: name, surname, birth, city, email, tel
    :return: Возвращает строковое значение
    """
    result = ''
    for keys, arg in kwargs.items():
        result += (f"{keys}: {arg}; ")
    return result

print(personal_data(name='Ivan', surname='Egorov', age=23, birth='11.10.1981', city='Moscow', email='i.egorov@domain.ru', tel='+7 (999) 111-11-11'))
