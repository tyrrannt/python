from time import sleep

# =============== 6.1 ==========================================================================================
class TrafficLight:
    _color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 10}
    __work_type = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def running(self):
        while True:
            for key in self.__work_type:
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

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"Фамилия: {self.surname} \nИмя: {self.name}\nДолжность: {self.position}"

    def get_total_income(self):
        return f"{self.get_full_name()} \nОбщий доход: {654}"


if __name__ == "__main__":
    print("Модуль для практических заданий 6-го урока")
