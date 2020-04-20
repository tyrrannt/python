# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

from lesson6 import TrafficLight, sleep

traffic = TrafficLight()

from tkinter import *
root = Tk()
myCanvas = Canvas(root)
myCanvas.pack()

def create_circle(x, y, r, canvasName, outline, fill): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, outline=outline, fill=fill)

def clicked(color1='', color2='', color3=''):
    create_circle(100, 50, 20, myCanvas, 'red', color1)
    create_circle(100, 100, 20, myCanvas, 'yellow', color2)
    create_circle(100, 150, 20, myCanvas, 'green', color3)

while 1:
    myCanvas.update_idletasks()
    myCanvas.update()
    sleep(0.01)
    #clicked()
