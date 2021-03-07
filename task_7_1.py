# __author__ Соловьева Дарья Викторовна
# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске
# (как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок
# под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и
# файлах (добавлять детали)?

import os

main_folder = "my_projekt"
folder_lst = ["settings", "mainapp", "adminapp", "authapp"]
for idx in range(len(folder_lst)):
    dir_path = os.path.join(main_folder, folder_lst[idx])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
