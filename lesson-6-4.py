# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from lesson6 import TownCar, SportCar, PoliceCar, WorkCar

town_car = TownCar('Черный', 'Mercedes-Benz C 200 4M Premium', 200)
sport_car = SportCar('Красный', 'Lamborghini aventador svj', 280)
police_car = PoliceCar('Белая', 'Лада Веста', 180)
work_car = WorkCar('Желтый', 'Тонар-7501', 60)

print("Симулятор автотранспорта. Управление: Клавиши от 1 до 4 выбор машины,")
print("e - запуск двигателя, q - остановка двигателя. a - поворот на лево, d - поворот на право")
print("w - педаль газа, s - педаль тормоза. i - информация о машине")
prototype = town_car
while True:
    action = input()
    if action != '':
        n = ord(action[0])
    else:
        continue
    if n == 49:
        prototype = town_car
        prototype.car_info()
    if n == 50:
        prototype = sport_car
        prototype.car_info()
    if n == 51:
        prototype = police_car
        prototype.car_info()
    if n == 52:
        prototype = work_car
        prototype.car_info()
    if n == 119:
        prototype.accelerator()
    if n == 115:
        prototype.brake()
    if n == 97:
        prototype.turn('лево')
    if n == 100:
        prototype.turn('право')
    if n == 101:
        prototype.go()
    if n == 113:
        prototype.stop()
    if n == 105:
        prototype.car_info()
    if n == 111:
        prototype.show_speed()
    if n == 27:
        break
