# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной
# папки в виде словаря, в котором ключи те же, а значения — списки вида
# [<files_quantity>, [<files_extensions_list>]], например:
#   {
#       100: [15, ['txt']],
#       1000: [3, ['py', 'txt']],
#       10000: [7, ['html', 'css']],
#       100000: [2, ['png', 'jpg']]
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
import os
from collections import defaultdict
import json

folder = r"D:\обучение\Основы языка Python\pythonProject"
dict_file_size = defaultdict(list)
for root, dirs, files in os.walk(folder):
    for file in files:
        name_file = os.path.join(root, file)
        file_size = os.stat(name_file).st_size
        if 0 <= file_size <= 10:
            dict_file_size[10].append(name_file[name_file.rfind("."):])
        elif 10 < file_size <= 100:
            dict_file_size[100].append(name_file[name_file.rfind("."):])
        elif 100 < file_size <= 1000:
            dict_file_size[1000].append(name_file[name_file.rfind("."):])
        elif 1000 < file_size <= 10000:
            dict_file_size[10000].append(name_file[name_file.rfind("."):])
        elif 10000 < file_size <= 100000:
            dict_file_size[100000].append(name_file[name_file.rfind("."):])
        elif 100000 < file_size <= 1000000:
            dict_file_size[1000000].append(name_file[name_file.rfind("."):])

new_dict_file_size = {}
for key, val in dict_file_size.items():
    new_dict_file_size.update({key: [len(val), val]})
# неотсортированный словарь
# print(new_dict_file_size)
list_keys = list(new_dict_file_size.keys())
list_keys.sort()
new_dict_file_size1 = {}
for i in list_keys:
    new_dict_file_size1.update({i: new_dict_file_size[i]})
# отсортированный словарь
print(new_dict_file_size1)
name_file_json = os.path.join(folder, "summary.json")
json_new_dict_file1 = json.dumps(new_dict_file_size1, indent=2)
with open(name_file_json, "w", encoding="UTF-8")as f:
    f.write(json_new_dict_file1)
