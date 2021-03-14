# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
# на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее
# сообщение и завершать скрипт.
import time


class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]

    def running(self):

        while TrafficLight.__color:
            print(TrafficLight.__color[0])
            time.sleep(7)
            print(TrafficLight.__color[1])
            time.sleep(3)
            print(TrafficLight.__color[2])
            time.sleep(4)

        # for color in TrafficLight.__color:
        #     if color == TrafficLight.__color[0]:
        #         print(color)
        #         time.sleep(7)
        #     elif color == TrafficLight.__color[1]:
        #         print(color)
        #         time.sleep(2)
        #     else:
        #         print(color)
        #         time.sleep(4)

a = TrafficLight()
a.running()