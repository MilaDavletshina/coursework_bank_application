import datetime
import pandas as pd
import json
from utils import get_exchange_rates, get_stock_api_price



def greeting():
    """Функция приветствия в зависимости от времени суток"""
    now = datetime.datetime.now()
    if 6 <= now.hour < 12:
        return "Доброе утро!"
    elif 12 <= now.hour < 18:
        return "Добрый день!"
    elif 18 <= now.hour < 24:
        return "Добрый вечер!"
    elif 0 <= now.hour < 6:
        return "Доброй ночи!"

# print(greeting())

# как вывести в красивый список, как округлить до двух знаков?
def card_operations_info(transactions):
    """Функция выводит общую информацию по карте"""
    data = pd.read_excel(transactions)

    cards = {}

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

    return {"cards": card_info}

transactions = 'data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls'
# print(card_operations_info(transactions))

def top_five_transactions(transactions):
    df = pd.read_excel(transactions)
    top_transactions = df.nlargest(5, "Сумма платежа")

    top_transactions_list = []
    for index, row in top_transactions.iterrows():
        data = {
            "date": row["Дата платежа"],
            "amount": row["Сумма платежа"],
            "category": row["Категория"],
            "description": row["Описание"]
        }
        top_transactions_list.append(data)
    return {"top_transactions": top_transactions_list}

transactions = 'data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls'
# print(top_five_transactions(transactions))

#как округлить до двух знаков?
def get_currency_rates(file):
    with open(file) as f:
        data = json.load(f)

    currency_list = data.get("user_currencies")
    usd = currency_list[0]
    eur = currency_list[1]
    currency_usd = get_exchange_rates(usd)
    currency_eur = get_exchange_rates(eur)

    usd_dict = {"currency": "USD", "rate": currency_usd}
    eur_dict = {"currency": "EUR", "rate": currency_eur}

    currency_list_exchange = [usd_dict, eur_dict]

    return {"currency_rates": currency_list_exchange}

file = "data/user_settings.json"
# print(get_currency_rates(file))


#как округлить до двух знаков?
def get_stocks_prices(file):
    with open(file) as f:
        data_stock = json.load(f)
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


file = "data/user_settings.json"
# print(get_stocks_prices(file))
