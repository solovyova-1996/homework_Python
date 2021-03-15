# __author__ Соловьева Дарья Викторовна
# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад
# и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии\
#     (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name.lower().capitalize()} {self.surname.lower().capitalize()}"

    def get_total_income(self):
        income_with_bonus = self._income["wage"] + self._income["bonus"]
        return income_with_bonus


position_1 = Position("aлександр", "Петров", "дворник", {"wage": 10, "bonus": 70})

print(position_1.name, position_1.surname, position_1.position)

print(position_1.get_full_name())
print(position_1.get_total_income())

position_2 = Position("Иван", "иванов", "разнорабочий", {"wage": 14, "bonus": 50})

print(position_2.name)
print(position_2.surname)
print(position_2.position)

print(position_2.get_full_name())
print(position_2.get_total_income())
