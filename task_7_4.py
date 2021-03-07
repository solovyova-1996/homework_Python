# __author__ Соловьева Дарья Викторовна
# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых
# не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os
from collections import defaultdict

folder = r"D:\обучение\Основы языка Python\pythonProject"
dict_file_size = defaultdict(list)
for root, dirs, files in os.walk(folder):
    for file in files:
        name_file = os.path.join(root, file)
        file_size = os.stat(name_file).st_size
        if 0 <= file_size <= 10:
            dict_file_size[10].append(name_file)
        elif 10 < file_size <= 100:
            dict_file_size[100].append(name_file)
        elif 100 < file_size <= 1000:
            dict_file_size[1000].append(name_file)
        elif 1000 < file_size <= 10000:
            dict_file_size[10000].append(name_file)
        elif 10000 < file_size <= 100000:
            dict_file_size[100000].append(name_file)
        elif 100000 < file_size <= 1000000:
            dict_file_size[1000000].append(name_file)
        else:
            print(name_file, file_size)

new_dict_file_size = {}
for key, val in dict_file_size.items():
    dict_file_size[key] = len(val)
    new_dict_file_size.update({key: dict_file_size[key]})
# print(new_dict_file_size)
list_keys = list(new_dict_file_size.keys())
list_keys.sort()
new_dict_file_size1 = {}
for i in list_keys:
    new_dict_file_size1.update({i: new_dict_file_size[i]})
print(new_dict_file_size1)
