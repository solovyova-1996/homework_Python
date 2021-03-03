# __author__ * Соловьева Дарья Викторовна
# 5. * Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует:
# ничего в файле не меняем, выводим сообщение в консоль.
import sys

with open("bakery.csv", "r", encoding="UTF-8") as f:
    lst_add_sale = f.readlines()
if len(sys.argv) <= 1:
    print("Введите номер записи и новую запись")
else:
    number_sale = int(sys.argv[1]) - 1
    new_sale = sys.argv[2]
    if len(lst_add_sale) < number_sale:
        print("Такой записи не существует")
    else:
        lst_add_sale[number_sale] = f"{new_sale}\n"
with open("bakery.csv", "w", encoding="UTF-8") as f:
    for line in lst_add_sale:
        f.writelines(line)
