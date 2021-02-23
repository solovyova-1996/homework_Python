# __author__ * Соловьева Дарья Викторовна
# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
# в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

from homework_Python.my_modules.utils import currency_rates

print(currency_rates("aud"))
print(currency_rates("inr"))
print(currency_rates("CAd"))
