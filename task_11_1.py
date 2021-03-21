# __author__Соловьева Дарья Викторовна
# 1. Реализовать класс
# «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:

    def __init__(self, data):
        if Data.valid(*Data.int_func(data)):
            self.data = data
        else:
            print("Ошибка, не валидная дата")

    @classmethod
    def int_func(cls, data):
        lst_data = data.split('-')
        return int(lst_data[0]), int(lst_data[1]), int(lst_data[2])

    @staticmethod
    def valid(day, month, year):
        if 0 < day < 31 and 0 < month < 13 and 0 < year < 2022:
            return True
        else:
            return False


f = Data("01-23-3333")
# print(f.data)
a = Data("01-12-1933")
print(a.data)
