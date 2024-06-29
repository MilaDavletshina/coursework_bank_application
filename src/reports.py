import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Optional

load_dotenv(".env")

def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция формирует отчет "траты по категориям" по заданной пользователем категории,
    в период за 3 месяца от указанной пользователем даты. Если дата отсутствует, то берется текущая дата """

    if date is None:
        date = datetime.now()
    else:
        date = datetime.strptime(date, '%d.%m.%Y')

    three_months_ago = date - timedelta(days=90)

    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'])
    filtered_transactions = transactions[(transactions['Дата операции'] >= three_months_ago) & (transactions['Категория'] == category)]

    filtered_transactions['Дата операции'] = filtered_transactions['Дата операции'].dt.strftime('%d.%m.%Y %H:%M:%S')
    return filtered_transactions[['Дата операции', 'Сумма операции', 'Категория']]

input_file = os.getenv("INPUT_FILE")
transactions = pd.read_excel(input_file)
category = "Супермаркеты"
date = "01.01.2024"

result = spending_by_category(transactions, category, date)
print(result)