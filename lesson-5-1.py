# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
fileD.close()

with open(r"my_text.txt", "a", encoding="UTF-8") as file_d:
    print("Вводите данные для записи в файл. Для выхода используйте пустую строку.")
    while True:
        content = input()
        if not content:
            break
        file_d.writelines(content)
    print("Конец фильма! :)")