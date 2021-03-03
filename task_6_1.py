# __author__ * Соловьева Дарья Викторовна
# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание:
# - код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# - Вы не знате заранее насколько идентичен шаблон строк файла. Попробуйте оценить это.
import requests

response = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
encodings = requests.utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

with open("github_com_file.txt", 'w', encoding="UTF-8") as f:
    f.write(content)
with open("github_com_file.txt", 'r', encoding="UTF-8") as f:
    lst_addr = []
    for line in f:
        line = line.strip()
        remote_addr = line[:line.find(" ")]
        requests_type = line[line.find('"') + 1:line.find('"') + 4]
        requested_resource = line[line.find('"') + 5: line.find('HTTP') - 1]
        tuple_addr = (remote_addr, requests_type, requested_resource)
        lst_addr.append(tuple_addr)
# lst_addr - это список кортежей, который требуется в условии
