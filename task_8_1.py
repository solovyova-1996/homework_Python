# __author__Соловьева Дарья Викторовна
# 1. Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает
# их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Уточнение
# Текст до собаки (Local-part): латинские буквы, цифры и символы: ' . _ + -
#
# Текст после собаки (Domain part): латинские буквы, цифры и символы . -
#
# В Domain part обязательно должна быть хотя бы одна точка.
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?


import re


def email_parse(email_address):
    email_search = re.search(r'(?P<username>[\w\d\'\.\_\+\-]+)@(?P<domain>[\w\d.-]+\.{1}\w{2,3})', email_address)
    try:
        email_dict = email_search.groupdict()
    except:
        raise ValueError(f"wrong email:{email_address}")
    return email_dict


email_parse_rez = email_parse("someone@geekbrains.ru")
print(email_parse_rez)
