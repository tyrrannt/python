"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
database = {}


def pass_gen(salt, passwd):
    """
    Генерирует hash сумму по двум аргументам
    :param salt: соль = строка UUID, универсальный уникальный идентификатор
    :param passwd: введенный пароль пользователя
    :return: возвращает HASH сумму (соль + пароль)
    """
    import hashlib
    byte_password = str.encode(passwd, encoding='utf-8')
    return hashlib.sha256(byte_password + salt.encode(encoding='utf-8')).hexdigest()


def pass_input(passwd, data):
    """
    Сохраняет пароль пользователя в словаре.
    :param passwd: введенный пароль пользователя
    :param data: хранилище паролей, словарь, ключем является соль, значением HASH сумма (соль + пароль)
    :return: Возвращает информационную строку с результатом работы функции.
    """
    import uuid

    salt = uuid.uuid4().hex

    for keys in data:
        if pass_gen(keys, passwd) == data[keys]:
            return 'Пароль имеется в базе данных'
    data[salt] = pass_gen(salt, passwd)
    return 'Пароль успешно записан'


while True:
    print('Для выхода введите q, для просмотра паролей в словаре - p')
    value = input('Введите пароль: ')
    if value == 'q':
        break
    if value == 'p':
        print(database)
        continue
    print(pass_input(value, database))
