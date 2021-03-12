# __author__Соловьева Дарья Викторовна
# 4. * Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения
# функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

from functools import wraps


def val_checker(func_bool):
    def val_checker_new(function):
        @wraps(function)
        def wrapper(x):
            if func_bool(x):
                rez = function(x)
                return rez
            else:
                raise ValueError(f"wrong val {x} ")

        return wrapper

    return val_checker_new


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


rezult = calc_cube(-3)
print(rezult)
