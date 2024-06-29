import pandas as pd
import os
import requests
from dotenv import load_dotenv
from log import setup_logger

log = logger.setup_applevel_logger(file_name = 'utils_log.log')
log = logger.get_logger(__name__)
load_dotenv(".env")


def read_excel_file(input_file):
    """ Функция считываест данные из excel файла"""
    excel_data = pd.read_excel(input_file)

    return excel_data

input_file = "data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls"
# print(read_excel_file(input_file))


def get_sort_dict(data, ascending=True):
    """Функция сортирует по убыванию по сумме платежа. Второй аргумент необязательный, задает порядок сортировки"""
    return sorted(data, key=lambda x: x.get("Сумма платежа", 0), reverse=ascending)

data = read_excel_file('data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls')
# result = get_sort_dict(data, True)
# print(result)


def get_exchange_rates(currency) -> float:
    """Функция получает курс валюты с сервера API"""

    API_KEY = os.getenv("API_KEY")

    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency}'

    response = requests.get(url)
    data = response.json()
    exchange_rates = data['conversion_rates']["RUB"]
    logger.info("Получен ответ с сервера")
    return exchange_rates

print(get_exchange_rates("EUR"))

def get_stock_api_price(stock) -> float:
    """Функция получаем стоимость акций с сервера API"""

    API_KEY_STOCK = os.getenv("API_KEY_STOCK")

    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={API_KEY_STOCK}'
    r = requests.get(url)
    data = r.json()
    stock_price = data['Global Quote']["05. price"]

    return stock_price

# print(get_stock_api_price("AAPL"))

