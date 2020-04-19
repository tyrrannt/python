# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

from lesson6 import Road

def price_format(price):
    if (price // 1000000000000) > 0:
        return round(price / 1000000000000, 3), "трлн."
    if (price // 1000000000) > 0:
        return round(price / 1000000000, 3), "млрд."
    if (price // 1000000) > 0:
        return round(price / 1000000, 3), "млн."
    if (price // 1000) > 0:
        return round(price / 1000, 3), "тыс."
count = 0
result = 1
my_road = []
while result:
    print("=========================================================================================")
    name = input("Введите наименование проекта дороги: ")
    try:
        road_len = float(input("Введите длинну дороги (км): "))
    except ValueError:
        print("Вместо цифр какая то фигня, значит длинна будет 500 км")
        road_len = 500
    try:
        while True:
            type_road = int(input("Введите тип дороги (1: Магистральные дороги, 2-3: Городские дороги, 4: Сельские дороги): "))
            if (round(type_road) <= 4) and (round(type_road) >= 1):
                type_road = round(type_road)
                break
    except ValueError:
        print("Вместо цифр какая то фигня, значит тип будет 1: Магистральные дороги")
        type_road = 1
    try:
        price = float(input("Введите цену 1 тонны дорожного полотна: "))
    except ValueError:
        print("Вместо цифр какая то фигня, значит цена будет 2600 руб")
        price = 2600.0

    my_road.append(Road(name, road_len, type_road))
    print(my_road[count].bulk(1))
    print(f"Для строительства дороги, на дорожное полотно потребуется {price_format(price * my_road[count].bulk())} рублей")
    print(my_road[count].road_info())
    print("=========================================================================================")
    result2 = 1
    while result2:
        variable = input("Выход - 1 или пустая строка; Продолжить - 2; Получить информацию о проведенных расчетах - 3: ")
        try:
            if int(variable) == 1:
                result = 0
                result2 = 0
            if int(variable) == 2:
                result2 = 0
        except ValueError:
            print("Неверный формат вариантов ответа, ожидается число от 1 до 3")
            continue
    count += 1
