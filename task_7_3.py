# __author__ Соловьева Дарья Викторовна
# 3. Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны
# в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены
# в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.
import shutil
import os

name_path = os.path.join("my_project", "templates")
name_path_auhapp = os.path.join("my_project", "authapp", "templates")
name_path_mainapp1 = os.path.join("my_project", "mainapp", "templates", "mainapp", "base.html")
name_path_mainapp2 = os.path.join("my_project", "mainapp", "templates", "mainapp", "index.html")
try:
    shutil.copytree(name_path_auhapp, name_path)
except FileExistsError:
    print(f"Директория {name_path_auhapp} существует")
dir_path_mainapp = os.path.join(name_path, "mainapp")
if not os.path.exists(dir_path_mainapp):
    os.makedirs(dir_path_mainapp)
shutil.copy2(name_path_mainapp1, dir_path_mainapp)
shutil.copy2(name_path_mainapp2, dir_path_mainapp)
