import pandas as pd
import os
import requests
from dotenv import load_dotenv

# from log import setup_logger

load_dotenv(".env")

# log = logger.setup_applevel_logger(file_name = 'utils_log.log')
# log = logger.get_logger(__name__)


input_file = os.getenv("INPUT_FILE")

def read_excel_file(input_file):
    """ Функция считываест данные из excel файла"""
    excel_data = pd.read_excel(input_file)

    return excel_data

# print(read_excel_file(input_file))


def get_exchange_rates(currency) -> float:
    """Функция получает курс валюты с сервера API"""

    API_KEY = os.getenv("API_KEY")

    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency}'

    response = requests.get(url)
    data = response.json()
    exchange_rates = data['conversion_rates']["RUB"]
    # logger.info("Получен ответ с сервера")
    return exchange_rates

# print(get_exchange_rates("EUR"))

def get_stock_api_price(stock) -> float:
    """Функция получаем стоимость акций с сервера API"""

    API_KEY_STOCK = os.getenv("API_KEY_STOCK")

    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={API_KEY_STOCK}'
    r = requests.get(url)
    data = r.json()
    stock_price = data['Global Quote']["05. price"]

    return stock_price

# print(get_stock_api_price("AAPL"))

