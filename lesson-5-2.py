# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open(r"text_2.txt", 'r', encoding='UTF-8') as file_d:
    my_list = []
    for i in file_d:
        my_list.append(len(i.split(' ')))
print(f"Строк в файле: {len(my_list)}, слов в строках: {my_list}")