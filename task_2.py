"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import defaultdict
from collections import Counter


list_obj = [list(Counter(input('Введите первое число: ')).elements()),
            list(Counter(input('Введите второе число: ')).elements())]

dict_obj = defaultdict(list)
dict_obj['first'] = list_obj[0]
dict_obj['second'] = list_obj[1]
dict_obj['summ'] = list(Counter(hex(int(''.join(dict_obj['first']),16) + int(''.join(dict_obj['second']), 16))).elements())[2:]
dict_obj['compositions'] = list(Counter(hex(int(''.join(dict_obj['first']),16) * int(''.join(dict_obj['second']), 16))).elements())[2:]
print(dict_obj['summ'], dict_obj['compositions'])




