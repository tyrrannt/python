# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open(r"text_3.txt", "r", encoding="UTF-8") as file_d:
    surname = ''
    prise = 0
    for i in file_d:
        surname, prise = i.split(" ")
        if float(prise) < 20000:
            print(f"Мне его жаль ===> {surname}. Понятия не имею как он живет на зп = {prise.strip(chr(10))}")
