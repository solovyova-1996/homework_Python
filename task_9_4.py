# __author__ Соловьева Дарья Викторовна
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


town_car = TownCar(100, "grey", "Honda", False)
print(town_car.max_speed, town_car.color, town_car.name, town_car.is_police)

town_car.go()
town_car.show_speed()
town_car.stop()
town_car.show_speed()

sport_car = SportCar(200, "rad", "Mitsubishi", False)
print(sport_car.max_speed, sport_car.color, sport_car.name, sport_car.is_police)

sport_car.go()
sport_car.show_speed()
sport_car.stop()
sport_car.turn("направо")

work_car = WorkCar(150, "orange", "Kamaz", False)
print(work_car.max_speed, work_car.color, work_car.name, work_car.is_police)

work_car.go()
work_car.show_speed()
work_car.stop()

police_car = PoliceCar(120, "blue", "BMW", True)
print(police_car.max_speed, police_car.color, police_car.name, police_car.is_police)

police_car.go()
police_car.show_speed()
police_car.turn("налево")
police_car.stop()
