# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

numerals = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open(r"text_4.txt", "r", encoding="UTF-8") as file_d:
    keys, splitter, value = '', '', ''
    for i in file_d:
        keys, splitter, value = i.split(' ')
        print(f"{numerals.get(keys)} {splitter} {value.strip(chr(10))}")
