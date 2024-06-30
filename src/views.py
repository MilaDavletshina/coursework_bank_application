import datetime
import pandas as pd
import json
import os
from dotenv import load_dotenv
from utils import get_exchange_rates, get_stock_api_price
from log import setup_logger

load_dotenv(".env")
input_file = os.getenv("INPUT_FILE")
currency_stock_file = os.getenv("CURRENCY_STOCK")

logger = setup_logger(datetime.datetime.now().strftime("%Y-%m-%d"))

def greeting():
    """Функция приветствия в зависимости от времени суток"""
    now = datetime.datetime.now()
    if 6 <= now.hour < 12:
        logger.info("Текущее состояние суток - утро")
        return "Доброе утро!"
    elif 12 <= now.hour < 18:
        logger.info("Текущее состояние суток - день")
        return "Добрый день!"
    elif 18 <= now.hour < 24:
        logger.info("Текущее состояние суток - вечер")
        return "Добрый вечер!"
    elif 0 <= now.hour < 6:
        logger.info("Текущее состояние суток - ночь")
        return "Доброй ночи!"

# print(greeting())


def card_operations_info(input_file):
    """Функция выводит общую информацию по карте"""
    data = pd.read_excel(input_file)

    cards = {}
    try:
        for index, row in data.iterrows():
            card_number = str(row['Номер карты'])[-4:] if pd.notnull(row['Номер карты']) else None
            total_spent = float(row['Сумма операции с округлением'])

            if card_number in cards:
                cards[card_number]['total_spent'] += total_spent
            else:
                cards[card_number] = {
                    'last_digits': card_number,
                    'total_spent': round(total_spent, 2),
                    'cashback': float(total_spent // 100)
                }

        card_info = [value for value in cards.values()]
        logger.info(f"Функция {card_operations_info} успешно реализована")
        return {"cards": card_info}
    except ValueError:
        logger.error("Проверьте формат загруженного файла!")
        return {}

# print(card_operations_info(input_file))

def top_five_transactions(input_file):
    """Функция выдает топ-5 транзакций по самой большой сумме платежа"""
    df = pd.read_excel(input_file)
    top_transactions = df.nlargest(5, "Сумма платежа")

    top_transactions_list = []
    try:
        for index, row in top_transactions.iterrows():
            data = {
                "date": row["Дата платежа"],
                "amount": row["Сумма платежа"],
                "category": row["Категория"],
                "description": row["Описание"]
            }
            top_transactions_list.append(data)
            logger.info(f"Функция {top_five_transactions} успешно реализована")
            return {"top_transactions": top_transactions_list}
    except ValueError:
        logger.error("Проверьте формат загруженного файла!")
        return []


# print(top_five_transactions(input_file))


def get_currency_rates(currency_stock_file):
    """Функция получает курсы валют"""
    try:
        with open(currency_stock_file) as f:
            data = json.load(f)
            logger.info(f"Файл {currency_stock_file} успешно загружен")
        currency_list = data.get("user_currencies")
        usd = currency_list[0]
        eur = currency_list[1]
        currency_usd = get_exchange_rates(usd)
        currency_eur = get_exchange_rates(eur)

        usd_dict = {"currency": "USD", "rate": currency_usd}
        eur_dict = {"currency": "EUR", "rate": currency_eur}

        currency_list_exchange = [usd_dict, eur_dict]

        return {"currency_rates": currency_list_exchange}
    except ValueError:
        logger.error("Проверьте формат загруженного файла!")
        return []

# print(get_currency_rates(currency_stock_file))


def get_stocks_prices(currency_stock_file):
    """Функция отображает стоимость акций"""
    try:
        with open(currency_stock_file) as f:
            data_stock = json.load(f)
            logger.info(f"Файл {currency_stock_file} успешно загружен")
            stock_list = data_stock.get("user_stocks")

            AAPL = stock_list[0]
            AMZN = stock_list[1]
            GOOGL = stock_list[2]
            MSFT = stock_list[3]
            TSLA = stock_list[4]

            stock_AAPL = get_stock_api_price(AAPL)
            stock_AMZN = get_stock_api_price(AMZN)
            stock_GOOGL = get_stock_api_price(GOOGL)
            stock_MSFT = get_stock_api_price(MSFT)
            stock_TSLA = get_stock_api_price(TSLA)

            AAPL_dict = {"stock": "AAPL", "price": stock_AAPL}
            AMZN_dict = {"stock": "AMZN", "price": stock_AMZN}
            GOOGL_dict = {"stock": "GOOGL", "price": stock_GOOGL}
            MSFT_dict = {"stock": "MSFT", "price": stock_MSFT}
            TSLA_dict = {"stock": "TSLA", "price": stock_TSLA}

            stocks_list_prices = [AAPL_dict, AMZN_dict, GOOGL_dict, MSFT_dict, TSLA_dict]

            return {"stock_prices": stocks_list_prices}
    except ValueError:
        logger.error("Проверьте формат загруженного файла!")
        return []

# print(get_stocks_prices(currency_stock_file))

