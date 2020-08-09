"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества
"""


def hash_gen(passwd):
    """
    Генерирует hash сумму
    :param passwd: введенный пароль пользователя
    :return: возвращает HASH сумму
    """
    import hashlib
    byte_password = str.encode(passwd, encoding='utf-8')
    return hashlib.sha256(byte_password).hexdigest()


string = 'youcan1'
set_hash = set()
set_str = set()

for i in range(len(string)):
    for j in range(len(string) - 1 if i == 0 else len(string), i, -1):
        set_hash.add(hash_gen(string[i:j]))
        set_str.add(string[i:j])
print("Количество различных подстрок:", len(set_hash))
print(set_str)
