from json import dump, load


# *************************************************  8.1  **************************************************************
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Dates:
    def __init__(self, date_str):
        self.date_string = date_str

    @classmethod
    def date_int(cls, date_str):
        err_result = 'Переданная дата не соответствует формату: 00-00-0000'
        date_list = date_str.split('-')
        if len(date_list) == 3:
            for i in range(0, len(date_list)):
                try:
                    date_list[i] = int(date_list[i])
                except ValueError:
                    return err_result
            return date_list
        else:
            return err_result

    def __str__(self):
        return f"{self.date_int(self.date_string)}"

    @staticmethod
    def valid_date(date_str):
        result = ''
        date_list = Dates.date_int(date_str)
        if len(date_list) == 3:
            result += 'День соответствует формату\n' if 0 < date_list[0] <= 31 else 'День не соответствует формату\n'
            result += 'Месяц соответствует формату\n' if 0 < date_list[1] <= 12 else 'Месяц не соответствует формату\n'
            result += 'Год соответствует формату\n' if 0 < date_list[2] < 9999 else 'Год не соответствует формату\n'
            return result
        else:
            return date_list


# *************************************************  8.2  **************************************************************
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class DivZero(Exception):
    def __init__(self, exc):
        self.exc = exc


class Division:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def processing(self):
        try:
            if self.second != 0:
                return self.first / self.second
            else:
                raise DivZero("Внимание, второй аргумент равен 0, возникает ситуация деления на 0!")
        except DivZero as dzero:
            return dzero
        except TypeError:
            return f"Не соответствие типов передаваемых аргументов. Ожидается число."


# *************************************************  8.3  **************************************************************
# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class IsNum:

    @staticmethod
    def completion():
        result = []
        count = 0
        print("Создание списка состоящего из одних цифр. Для выхода введите слово - stop")
        while True:
            user_input = input(f'{count}.) ')
            if user_input == 'stop':
                break
            if user_input.isdigit():
                result.append(int(user_input))
            else:
                print('Введено не число!')
                continue
            count += 1
        return result


# *************************************************  8.4  **************************************************************
# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
"""
    def profit(self, nom, nom_dict, count):
        if nom in self.nom.keys():
            nom_list = self.nom.get(nom)
            self.nom.update({nom: [nom_dict, nom_list[1] + count]})
            self.remains += count
        else:
            self.nom.update({nom: [nom_dict, count]})
            self.remains += count
            
    def cost(self, nom, nom_dict, count):
        if nom in self.nom.keys():
            nom_list = self.nom.get(nom)
            if nom_list[1] >= count:
                self.nom.update({nom: [nom_dict, nom_list[1] - count]}) \
                    if (nom_list[1] - count) > 0 else self.nom.pop(nom)
                self.remains -= count
            else:
                print(
                    f"Остаток номенклатуры на складе {nom_list[1]} не хватает {count - nom_list[1]}.")
        else:
            print(f"Номенклатуры {nom.nom} на складе нет.")
"""


def profit_loc(nom, nom_dict, count, self_nom, self_remains):
    if nom in self_nom.keys():
        nom_list = self_nom.get(nom)
        self_nom.update({nom: [nom_dict, nom_list[1] + count]})
        self_remains += count
    else:
        self_nom.update({nom: [nom_dict, count]})
        self_remains += count


def cost_loc(nom, nom_dict, count, self_nom, self_remains):
    if nom in self_nom.keys():
        nom_list = self_nom.get(nom)
        if nom_list[1] >= count:
            self_nom.update({nom: [nom_dict, nom_list[1] - count]}) \
                if (nom_list[1] - count) > 0 else self_nom.pop(nom)
            self_remains -= count
        else:
            print(
                f"Остаток номенклатуры на складе {nom_list[1]} не хватает {count - nom_list[1]}.")
    else:
        print(f"Номенклатуры {nom.nom} на складе нет.")


class Warehouse84:
    remains = 0
    nom = {}

    def __init__(self, title):
        self.title = title

    def __str__(self):
        result = ''
        for i in self.nom:
            result += f"{self.nom.get(i)[0]} в количестве {self.nom.get(i)[1]}\n"
        return f"{'*' * 35} \nНаименование склада: {self.title} \nОстатки на складе: {self.remains}" \
               f" \n{result} \n{'*' * 35}"

    def profit(self, nom, nom_dict, count):
        profit_loc(nom, nom_dict, count, self.nom, self.remains)

    def cost(self, nom, nom_dict, count):
        cost_loc(nom, nom_dict, count, self.nom, self.remains)

    def save(self, filename):
        with open(filename, 'w', encoding='UTF-8') as file_j:
            dump(self.nom, file_j)

    def read(self, filename):
        try:
            with open(filename, 'r+', encoding='UTF-8') as file_j:
                self.nom = load(file_j)
                self.remains = self.counts(self.nom)
        except FileNotFoundError:
            self.nom = {}

    @staticmethod
    def counts(dicts):
        result = 0
        for i in dicts:
            result += dicts.get(i)[1]
        return result


class OfficeEquipment84:
    def __init__(self, nom, equip_type, equip_name, equip_article, equip_weight):
        self.nom = nom
        self.equip_type = equip_type
        self.equip_name = equip_name
        self.equip_article = equip_article
        self.equip_weight = equip_weight

    def __str__(self):
        return f'{"*" * 35}\n{self.equip_type}\n{self.equip_name}\n{self.equip_article}\n{self.equip_weight}\n{"*" * 35}'

    def profit_wharehouse(self):
        return {'Тип': self.equip_type, 'Наименование': self.equip_name, 'Артикул': self.equip_article,
                'Вес': self.equip_weight, }

    def __repr__(self):
        return self.nom


class Units:
    remains = 0
    division = {}
    nom = {}

    def __init__(self, title):
        self.title = title

    def profit(self, nom, nom_dict, count):
        profit_loc(nom, nom_dict, count, self.nom, self.remains)

    def cost(self, nom, nom_dict, count):
        cost_loc(nom, nom_dict, count, self.nom, self.remains)


# *************************************************  8.5  **************************************************************
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.


# *************************************************  8.6  **************************************************************
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.


# *************************************************  8.7  **************************************************************
# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imaginary = imaginary_part

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(((self.real * other.real) - (self.imaginary * other.imaginary)),
                       ((self.real * other.imaginary) + (self.imaginary * other.real)))

    def __truediv__(self, other):
        return Complex((((self.real * other.real) + (self.imaginary * other.imaginary)) / (
                (other.real ** 2) + (other.imaginary ** 2))),
                       (((self.real * other.imaginary) - (self.imaginary * other.real)) / (
                               (other.real ** 2) + (other.imaginary ** 2))) * -1)

    def __str__(self):
        return f"{self.real} {'+' if self.imaginary > 0 else '-'} {abs(self.imaginary)}i"
