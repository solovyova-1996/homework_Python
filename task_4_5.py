# __author__ * Соловьева Дарья Викторовна
# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

import sys
from homework_Python.my_modules.utils import currency_rates

command = sys.argv[1]
print(currency_rates(command))
