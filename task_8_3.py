# __author__Соловьева Дарья Викторовна
# 3.Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
from functools import wraps


def type_logger(func):
    @wraps(func)
    def type_logger_wraper(*args):
        for item in func(*args):
            print(f"{func.__name__}({item} : {type(item)})")

    return type_logger_wraper


@type_logger
def calc_cube(*args):
    return args


calc_cube(3, -2, [1], 'a', 12.12, True, calc_cube)
