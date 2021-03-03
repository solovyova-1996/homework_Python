# __author__ * Соловьева Дарья Викторовна
# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным
# файла логов из предыдущего задания. Спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Примечание:
# - Уверены ли вы, что максимальное кол-во запросов - уникально?
# Т.е. найденный спамер - только один? Или таких спамеров может быть несколько?
import requests
import json

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
        lst_addr.append(remote_addr)

lst_addr_json = json.dumps(lst_addr, ensure_ascii=False, indent=2)
with open("ip.json", "w", encoding="UTF-8") as f:
    f.write(lst_addr_json)
with open("ip.json", "r", encoding="UTF-8") as f:
    lst_addr_json = f.read()
    lst_addr = json.loads(lst_addr_json)
    dict_number_request_ip = {}
    for ip in lst_addr:
        number_request_ip = lst_addr.count(ip)
        dict_number_request_ip.update({ip: number_request_ip})
dict_number_request_ip_json = json.dumps(dict_number_request_ip, ensure_ascii=False, indent=2)
with open("dict_number_request_ip.json", "w", encoding="UTF-8") as f:
    f.write(dict_number_request_ip_json)
with open("dict_number_request_ip.json", "r", encoding="UTF-8") as f:
    dict_number_request_ip_json = f.read()
    dict_number_request_ip = json.loads(dict_number_request_ip_json)
    count_request_ip_list = []
    for val in dict_number_request_ip.values():
        val = int(val)
        count_request_ip_list.append(val)
    max_count = max(count_request_ip_list)
    for key in dict_number_request_ip.keys():
        if dict_number_request_ip[key] == max_count:
            ip_spam = key
            break

print(f" IP спамера: {ip_spam}, количество запросов: {dict_number_request_ip[ip_spam]}")
