"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
from collections import namedtuple


class Basic(namedtuple("BasicNode", ["left", "right"])):
    def walk(self, dict_obj, pref):
        self.left.walk(dict_obj, pref + "0")
        self.right.walk(dict_obj, pref + "1")


class Final(namedtuple("FinalNode", ["symbol"])):
    def walk(self, dict_obj, pref):
        dict_obj[self.symbol] = pref or "0"


def huff_enc(origin_string):
    from collections import Counter
    import heapq
    """
    Функция кодирующая строку в код Хаффмана. Будем использовать кучу для построения очереди с приоритетами, которую
    будем строить с помощью цикла for
    :param origin_string: Исходная строка
    :return: Возвращается словарь состоящий из символов и кодов которые им соответствуют
    """
    queue = []
    for symbol, freq in Counter(origin_string).items():
        queue.append((freq, len(queue), Final(symbol)))
    heapq.heapify(queue)
    count = len(queue)
    while len(queue) > 1:
        left_frequency, first, left = heapq.heappop(queue)
        right_frequency, second, right = heapq.heappop(queue)
        heapq.heappush(queue, (left_frequency + right_frequency, count, Basic(left, right)))
        count += 1
    dict_obj = {}
    print(queue)
    if queue:
        [(freq, count, root)] = queue
        root.walk(dict_obj, "")
    return dict_obj


def huff_dec(str_obj, dict_obj):
    """
    Декодирование строки по кодам Хаффмана
    :param str_obj: закодированная строка
    :param dict_obj: Словарь кодов
    :return: Возвращаем раскодированную строку
    """

    result = []
    sub_str = ""
    for symbol in str_obj:
        sub_str += symbol
        for key in dict_obj:
            if dict_obj.get(key) == sub_str:
                result.append(key)
                sub_str = ""
                break
    return "".join(result)


def main():
    str_obj = input('Введите строку: ')
    huff_code = huff_enc(str_obj)
    enc_str = "".join(huff_code[symbol] for symbol in str_obj)
    print(len(huff_code), len(enc_str))
    for symbol in sorted(huff_code):
        print(f"{symbol}: {huff_code[symbol]}")
    print(enc_str)
    print(huff_code)
    assert huff_dec(enc_str, huff_code) == str_obj
    print(huff_dec(enc_str, huff_code))



if __name__ == "__main__":
    main()
