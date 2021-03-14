# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
class Car:
    def __init__(self, max_speed, color, name, is_police, speed=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.max_speed = max_speed

    def go(self):
        self.speed = self.max_speed
        print(f"Машина поехала")

    def stop(self):
        self.speed = 0
        print(f"Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        else:
            print(f"Текущая скорость автомобиля {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")
        else:
            print(f"Текущая скорость автомобиля {self.speed}")


class PoliceCar(Car):
    pass


a = TownCar(777, "grun", "honda", False)
a.show_speed()
a.go()
a.show_speed()
a.stop()
a.show_speed()
