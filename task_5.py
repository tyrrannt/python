"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class stack_plates:
    count = 0
    max_size = 20

    def __init__(self):

        self.id = stack_plates.count
        self.summ = []
        stack_plates.count += 1

    def __del__(self):
        stack_plates.count -= 1

    def add_plates(self, name='Блюдце'):
        if len(self.summ) < stack_plates.max_size:
            self.summ.append(name)
        else:
            print(f"Стопка заполнена")

    def del_plates(self):
        if len(self.summ) != 0:
            self.summ.pop()
        else:
            print(f"Стопка пуста")

    def get_len(self):
        return len(self.summ)

    def __str__(self):
        return f"Номер стопки {self.id}, Количество тарелок {len(self.summ)}"


plates = []
counter = 0

while True:
    a = input("Добавление - i, Удаление - d, Добавление стопки - a, Удаление стопки - r, Выход - q:   ")
    if a == 'w':
        if len(plates) == 0:
            print(f"Для начала необходимо создать стопку")
        else:
            plates[counter].add_plates()
            print(plates[counter])
    elif a == 's':
        if len(plates) == 0:
            print(f"Для начала необходимо создать стопку")
        else:
            plates[counter].del_plates()
            print(plates[counter])
    elif a == 'a':
        if len(plates) == 0:
            plates.append(stack_plates())
            counter = 0
            print(f"Стопка №{counter} успешно добавлена")
        elif plates[counter].get_len() == 20:
            plates.append(stack_plates())
            counter += 1
        else:
            print(f"Стопка не заполнена, добавление новой не возможно")
    elif a == 'd':
        if counter >= 0:
            if plates[counter].get_len() == 0:
                plates.pop()
                print(f"Стопка №{counter} успешно удалена")
                counter -= 1
            else:
                print(f"Стопка не пуста, удаление невозможно")
        else:
            print(f"Стопки отсутствуют")
    elif a == 'i':
        print(f"Количество стопок {len(plates)}")
    elif a == 'q':
        break
