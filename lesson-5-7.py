# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

from functools import reduce
from json import dump, load


def num_list(x, y):
    return x + y


firm_dict = {}
average = []
with open(r"text_7.txt", "r", encoding='UTF-8') as file_d:
    for i in file_d:
        i = i.strip(chr(10))
        firms = i.split()
        firm_dict.update({firms[0]: (float(firms[2]) - float(firms[3]))})
        if firm_dict.get(firms[0]) > 0:
            average.append(firm_dict.get(firms[0]))
    jsons = [firm_dict, {"average_profit": round((reduce(num_list, average) / len(average)), 2)}]

print(f"Полученный список, передаваемый на запись в JSON файл - {jsons}")
with open("text_7.json", "w", encoding='UTF-8') as file_d:
    dump(jsons, file_d)

with open("text_7.json", "r", encoding='UTF-8') as file_d:
    print(f"Считываем содержимое из JSON файла - {load(file_d)}")
