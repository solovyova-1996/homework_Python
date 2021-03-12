# __author__Соловьева Дарья Викторовна
# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации
# вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" ' \
#       '"Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?
import re

with open("log.txt", "r", encoding="UTF-8") as f:
    error_line = []
    for line in f:
        try:
            parsed_raw = re.search(
                r"(\d+.\d+.\d+.\d+)[\s-]+\[(.+)\]\s+\"(\w+)\s+([\/\w\d]+)\s+[\/\w\d.\"]+\s+(\d+)\s+(\d+)", line)
            print(parsed_raw.group(1, 2, 3, 4, 5, 6))
        except:
            error_line.append(line)

print(error_line)
print(len(error_line))
