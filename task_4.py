"""
Задание 4.
Реализуйте скрипт "Кеширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
cash = {}


def parse(url, item):
    from urllib.parse import urlparse
    url_str = urlparse(url)
    return str(url_str[item])


def url_gen(url, salt=0):
    """
    Генерирует hash сумму по двум аргументам
    :param salt: если 0 то возвращается (соль + пароль), иначе только соль
    :param url:  url-адрес
    :return: возвращает HASH суммы соль или (соль + пароль) в зависимости от запроса, где солью является название домена
    """
    import hashlib

    byte_salt = str.encode(parse(url, 1), encoding='utf-8')
    byte_url = str.encode(url, encoding='utf-8')
    if salt == 0:
        return hashlib.sha256(byte_url + byte_salt).hexdigest()
    else:
        return hashlib.sha256(byte_salt).hexdigest()


def url_input(url, data):
    """
    Сохраняет url пользователя в словаре.
    :param url: введенный url пользователя
    :param data: кэш страниц, словарь, ключем является домен, значением список HASH сумм (соль + пароль)
    :return: Возвращает информационную строку с результатом работы функции. И выводит сгенерированный hash
    """
    values = []
    if url_gen(url, 1) in data.keys():
        values = data[url_gen(url, 1)]
        for items in values:
            if url_gen(url) == items:
                return 'Страничка имеется в базе данных'
            else:
                values.append(url_gen(url))
                data[url_gen(url, 1)] = values
                return 'Страница добавлена в кэш. Hash = ' + url_gen(url, 1)
    values.append(url_gen(url))
    data[url_gen(url, 1)] = values
    return 'Страница успешно записана. Hash = ' + url_gen(url, 1)


while True:
    print('Для выхода введите q, для просмотра содержимого кэша - p')
    value = input('Введите URL: ')
    if value == 'q':
        break
    if value == 'p':
        print(cash)
        continue
    print(url_input(value, cash))
