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


S = 'youcan'
set_hash = set()
set_str = set()

for i in range(len(S)):
    for j in range(len(S) - 1 if i == 0 else len(S), i, -1):
        set_hash.add(hash_gen(S[i:j]))
        set_str.add(S[i:j])
print("Количество различных подстрок:", len(set_hash))
print(set_str)
