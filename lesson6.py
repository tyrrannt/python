from itertools import cycle
from time import sleep


# =============== 6.1 ==========================================================================================
class TrafficLight:
    _color = {'red': 7, 'yellow': 2, 'green': 10}
    __work_type = ['red', 'yellow', 'green', 'yellow']

    def running(self):
        for key in cycle(self.__work_type):
            print(key)
            sleep(self._color.get(key))


# =============== 6.2 ===========================================================================================
class Road:
    _type_road = {
        1: {'Тип': 'Магистральные дороги', 'Полотно': 1, 'Толщина': 0.05, 'Полосы': 4, 'Ширина': 0},
        2: {'Тип': 'Городские дороги', 'Полотно': 1, 'Толщина': 0.04, 'Полосы': 2, 'Ширина': 0},
        3: {'Тип': 'Городские дороги', 'Полотно': 2, 'Толщина': 0.24, 'Полосы': 2, 'Ширина': 1},
        4: {'Тип': 'Сельские дороги', 'Полотно': 3, 'Толщина': 0.15, 'Полосы': 2, 'Ширина': 1}
    }
    __type_of_roadbed = {1: {'Тип': 'асфальт', 'Вес': 2300}, 2: {'Тип': 'бетон', 'Вес': 2180},
                         3: {'Тип': 'щебень', 'Вес': 1400}}
    __width_road_lane = [3.75, 3.0]

    count = 0

    def __init__(self, name, length, type_of_road):
        self._name = name
        self._length = length * 1000
        self._type_of_road = type_of_road
        Road.count += 1

    def values(self, name_value):
        return self._type_road.get(self._type_of_road).get(name_value)

    def road_info(self):
        print(f"Характеристики дороги:")
        for key, value in self._type_road.get(self._type_of_road).items():
            if key == 'Полотно':
                value = self._type_of_roadbed(value, 1)
            if key == 'Ширина':
                value = self._width_road_lane(1)
            print(key, ': ', value)
        return self.count

    def _width_road_lane(self, info=0):
        if info == 0:
            return self.__width_road_lane[self.values('Ширина')] * self.values('Полосы')
        else:
            return str(self.__width_road_lane[self.values('Ширина')] * self.values('Полосы')) + ' метров'

    def _type_of_roadbed(self, type_rb, info=0):
        if info == 0:
            return self.__type_of_roadbed.get(type_rb).get('Вес')
        else:
            return self.__type_of_roadbed.get(type_rb)

    def bulk(self, info=0):
        if info == 0:
            return (self._length * self.values('Толщина') * self._width_road_lane() *
                    self._type_of_roadbed(self.values('Полотно'))) / 1000
        else:
            mass = (self._length * self.values('Толщина') * self._width_road_lane() *
                    self._type_of_roadbed(self.values('Полотно'))) / 1000
            return f"Для {self.values('Тип')} длинной {self._length} метров, потребуется {mass} тонн"


# =============== 6.3 ==========================================================================================
class Worker:
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        super()._income['wage'] = wage
        super()._income['bonus'] = bonus

    def get_full_name(self):
        return f"Фамилия: {self.surname} \nИмя: {self.name}\nДолжность: {self.position}"

    def get_total_income(self):
        return f"{self.get_full_name()} \nОбщий доход: {super()._income.get('wage') + super()._income.get('bonus')}"


# =============== 6.4 ==========================================================================================
class Car:
    _turn = ''

    def __init__(self, car_color, car_name, max_speed, car_police, car_speed=0, engine=0):
        self.speed = car_speed
        self.color = car_color
        self.name = car_name
        self.is_police = car_police
        self.engine = engine
        self.mspeed = max_speed

    def go(self):
        if self.engine == 0:
            self.engine = 1
            return print(f"Двигатель заведен!")
        else:
            return print(f"Двигатель уже заведен!")

    def stop(self):
        if self.engine == 1:
            if self.speed == 0:
                self.engine = 0
                return print(f"Двигатель выключен!")
            else:
                return print(f"Для остановки автомобиля необходимо остановить движение!")
        else:
            return print(f"Двигатель уже выключен!")

    def accelerator(self):
        if self.engine == 1:
            if self.speed < int(self.mspeed):
                self.speed += 10
                self._turn = ''
            else:
                return print(f'Скорость автомобиля {self.speed} км/ч превысила допустимый предел {self.mspeed}')
            return print(f'Скорость автомобиля {self.name} = {self.speed}')
        else:
            return print('Двигатель выключен! Для началадвижения заведите автомобиль.')

    def brake(self):
        if self.speed >= 10:
            self.speed -= 10
            return print(f'Скорость автомобиля {self.name} = {self.speed}')
        else:
            return print(f"Автомобиль {self.name} уже остановлен!")

    def turn(self, car_turn):
        if self.speed > 0:
            self._turn = car_turn
            return print(f"Автомобиль {self.name} повернул на {car_turn}.")
        else:
            return print(f"Автомобиль {self.name} на данный момент припаркован. Повороты в таком состоянии недоступны")

    def show_speed(self):
        return self.speed

    def car_info(self):
        return print(
            f"Автомобиль: {self.name}\nЦвет: {self.color}\nСостояние: {f'Движется. Скорость = {self.speed}' if self.speed > 0 else 'Припаркована'}\n Тип: {f'Машина полиции ' if self.is_police else 'Гражданский автомобиль'}\n")


class TownCar(Car):
    def __init__(self, car_color, car_name, mspeed, car_police=False, car_speed=0):
        super().__init__(car_color, car_name, mspeed, car_police, car_speed=0)

    def show_speed(self):
        if self.speed <= 60:
            return print(f"Скорость автомобиля {self.name} равна {self.speed}")
        else:
            return print(f"Внимание!!! Превышение скорости автомобиля {self.name} на {self.speed - 60}!!!!")


class SportCar(Car):
    def __init__(self, car_color, car_name, mspeed, car_police=False, car_speed=0):
        super().__init__(car_color, car_name, mspeed, car_police, car_speed=0)

    pass


class WorkCar(Car):
    def __init__(self, car_color, car_name, mspeed, car_police=False, car_speed=0):
        super().__init__(car_color, car_name, mspeed, car_police, car_speed=0)

    def show_speed(self):
        if self.speed <= 40:
            return print(f"Скорость автомобиля {self.name} равна {self.speed}")
        else:
            return print(f"Внимание!!! Превышение скорости автомобиля {self.name} на {self.speed - 40}!!!!")


class PoliceCar(Car):
    def __init__(self, car_color, car_name, mspeed, car_police=True, car_speed=0):
        super().__init__(car_color, car_name, mspeed, car_police, car_speed=0)

    pass


# =============== 6.4 ==========================================================================================
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Название: {self.title}. Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Название: {self.title}. Пишем авторучкой!")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Название: {self.title}. Пишем карандашом!")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Название: {self.title}. Пишем маркером!")


if __name__ == "__main__":
    print("Модуль для практических заданий 6-го урока")
    color = {'red': 7, 'yellow': 2, 'green': 10}
    work_type = ['red', 'yellow', 'green', 'yellow']


    def run():
        for key in cycle(work_type):
            yield key, color.get(key)


    a = run()
    print(next(a))
