import os
import json
import pandas as pd
import datetime
from dotenv import load_dotenv
from reports import spending_by_category
from services import person_money_transfer
from views import get_greeting, card_operations_info, top_five_transactions, get_currency_rates, get_stocks_prices



load_dotenv(".env")
input_file = os.getenv("INPUT_FILE")
currency_stock_file = os.getenv("CURRENCY_STOCK")

API_KEY = os.getenv("API_KEY")
API_KEY_STOCK = os.getenv("API_KEY_STOCK")


def main():
    """Основная функция для вывода данных в json"""

    greeting = get_greeting()
    card_info = card_operations_info(input_file)
    top_five = top_five_transactions(input_file)
    currency_rate = get_currency_rates(currency_stock_file)
    stock_prices = get_stocks_prices(currency_stock_file)


    user_info = {
        "greeting": greeting,
        "card_info": card_info,
        "top_five": top_five,
        "currency_rate": currency_rate,
        "stock_prices": stock_prices
    }


    return json.dumps(user_info, ensure_ascii=False, indent=4)






if __name__ == "__main__":
    print(main())

    money_transfer = person_money_transfer(input_file)

    transactions = pd.read_excel(input_file)
    spending = spending_by_category(transactions, 'Супермаркеты')

    print("Отчет. Переводы физическим лицам")
    print(money_transfer)
    print("Отчет. Траты по категориям")
    print(spending)