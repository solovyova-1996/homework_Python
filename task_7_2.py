# __author__ Соловьева Дарья Викторовна
# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер
# для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно
# создать в любом текстовом редакторе «руками» (не программно);
# Подумайте о возможных исключительных ситуациях при работе скрипта.
# Усложнение Библиотеки для парсинга yaml использовать нельзя
import os

with open("config.yaml", "r", encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if not os.path.exists(line):
            if "." in line:
                with open(line.strip(), "w", encoding="UTF-8") as f:
                    pass
            else:
                os.makedirs(line.strip())
# Сделала название главной папки my_proect1 потому что это задание выполняла последним и уже использовала my_project
# Насчет структуры файла config.yaml долго думала, ничего не получалось,
# не считается ли неправильной та структура,которую я сделала?