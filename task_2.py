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

def pass_input(database):
    import hashlib, uuid

    value = input('Введите пароль: ')
    salt = uuid.uuid4().hex
    byte_password = str.encode(value, encoding='utf-8')
    sha = hashlib.sha256(byte_password+salt.encode( encoding='utf-8')).hexdigest()
    if sha in database.values():
        print('Пароль имеется в базе данных')
    else:
        database[salt] = sha
    return database

print(pass_input(database))  # '422fbfbc67fe17c86642c5eaaa48f8b670cbed1b'