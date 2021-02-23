# __author__ * Соловьева Дарья Викторовна
# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...) и
# возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос
# к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str,
# решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
# величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента
# передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
# регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
import requests.utils

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
encodings = requests.utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(currency_code):
    idx_curency_code = content.find(currency_code.upper())
    if idx_curency_code == -1:
        return None
    else:
        idx_value = content[idx_curency_code:].find("<Value>")
        begin_idx = idx_curency_code + idx_value + 7
        end_idx = content[begin_idx:].find("</Value>")
        exchange_rate_in_rubles_str = content[begin_idx:begin_idx + end_idx]
        exchange_rate_in_rubles_1 = exchange_rate_in_rubles_str[:exchange_rate_in_rubles_str.index(",")]
        exchange_rate_in_rubles_2 = exchange_rate_in_rubles_str[exchange_rate_in_rubles_str.index(",") + 1:]
        exchange_rate_in_rubles = f"{exchange_rate_in_rubles_1}.{exchange_rate_in_rubles_2}"
        exchange_rate_in_rubles = float(exchange_rate_in_rubles)
        return exchange_rate_in_rubles


print(currency_rates("GBP"))
print(currency_rates("eur"))
print(currency_rates("uSd"))
