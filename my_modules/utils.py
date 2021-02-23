import requests.utils
import datetime

dict_month = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
              "Sept": 9, "Ost": 10, "Now": 11, "Dec": 12}


def currency_rates(currency_code):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    headers = response.headers
    date_str = headers["Date"][5:16]
    year = int(date_str[7:])
    month = dict_month[date_str[3:6]]
    day = int(date_str[:3])
    date_change = datetime.date(year, month, day)
    idx_curency_code = content.find(currency_code.upper())
    if idx_curency_code == -1:
        return None, date_change
    else:
        idx_value = content[idx_curency_code:].find("<Value>")
        begin_idx = idx_curency_code + idx_value + 7
        end_idx = content[begin_idx:].find("</Value>")
        exchange_rate_in_rubles_str = content[begin_idx:begin_idx + end_idx]
        exchange_rate_in_rubles_1 = exchange_rate_in_rubles_str[:exchange_rate_in_rubles_str.index(",")]
        exchange_rate_in_rubles_2 = exchange_rate_in_rubles_str[exchange_rate_in_rubles_str.index(",") + 1:]
        exchange_rate_in_rubles = float(f"{exchange_rate_in_rubles_1}.{exchange_rate_in_rubles_2}")
        return exchange_rate_in_rubles, date_change