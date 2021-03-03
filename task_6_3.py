# __author__ * Соловьева Дарья Викторовна
# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий
# из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся
# ФИО значение в словаре - None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# Примечание: При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи
import json

with open("user.csv", 'r', encoding='UTF-8') as f:
    name_lst = f.readlines()
    name_lst_clear = []
    for name in name_lst:
        name_clear = name.strip().replace(",", " ")
        name_lst_clear.append(name_clear)

with open("hobby.csv", 'r', encoding='UTF-8') as f:
    hobby_lst = f.readlines()
    hobby_lst_clear = []
    for hobby in hobby_lst:
        hobby_clear = hobby.strip()
        hobby_lst_clear.append(hobby_clear)


def dict_name_hobby_create(name_lst, hobby_lst):
    dict_name_hobby = {}
    for i in range(len(name_lst)):
        if len(hobby_lst) == 0:
            dict_name_hobby.update({name_lst.pop(0): None})
        else:
            dict_name_hobby.update({name_lst.pop(0): hobby_lst.pop(0)})
    if len(name_lst) < len(hobby_lst):
        print("1")
    return dict_name_hobby


name_hobby_dict = dict_name_hobby_create(name_lst_clear, hobby_lst_clear)
print(name_hobby_dict)
name_hobby_dict_json = json.dumps(name_hobby_dict, ensure_ascii=False, indent=2)
with open("dict_name_hobby.json", 'w', encoding='UTF-8') as f:
    f.write(name_hobby_dict_json)
with open("dict_name_hobby.json", 'r', encoding='UTF-8') as f:
    name_hobby_dict_json = f.read()
    name_hobby_dict = json.loads(name_hobby_dict_json)
print(name_hobby_dict)
