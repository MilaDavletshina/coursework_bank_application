import datetime
import pandas as pd
import os
import requests
from dotenv import load_dotenv
from log import setup_logger


load_dotenv(".env")
input_file = os.getenv("INPUT_FILE")

logger = setup_logger(datetime.datetime.now().strftime("%Y-%m-%d"))

def read_excel_file(input_file):
    """ Функция считываест данные из excel файла"""
    try:
        excel_data = pd.read_excel(input_file)
        logger.info(f"Функция {read_excel_file} успешно реализована")
        return excel_data
    except ValueError:
        logger.error("Проверьте формат загруженного файла!")
        return []

# print(read_excel_file(input_file))


def get_exchange_rates(currency) -> float:
    """Функция получает курс валюты с сервера API"""

    API_KEY = os.getenv("API_KEY")

    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency}'
    try:
        response = requests.get(url)
        data = response.json()
        exchange_rates = data['conversion_rates']["RUB"]
        logger.info("Ответ с сервера API получен")
        return exchange_rates
    except ValueError:
        logger.error("Ошибка загрузки. Проверьте введенные данные.")
        return "Ошибка загрузки. Проверьте введенные данные."
# print(get_exchange_rates("EUR"))

def get_stock_api_price(stock) -> float:
    """Функция получаем стоимость акций с сервера API"""

    API_KEY_STOCK = os.getenv("API_KEY_STOCK")

    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={API_KEY_STOCK}'
    try:
        r = requests.get(url)
        data = r.json()
        stock_price = data['Global Quote']["05. price"]
        logger.info("Ответ с сервера API получен")
        return stock_price
    except ValueError:
        logger.error("Ошибка загрузки. Проверьте введенные данные.")
        return "Ошибка загрузки. Проверьте введенные данные."

# print(get_stock_api_price("AAPL"))

