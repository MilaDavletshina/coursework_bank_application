import pandas as pd
import os
import requests
from dotenv import load_dotenv

def read_excel_file(input_file):
    """ Считывание excel файла и преобразование в словарь"""
    df = pd.read_excel(input_file)
    df_dict = df.to_dict(orient="records")
    return df_dict

# input_file = "data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls"
# print(read_excel_file(input_file))


def get_sort_dict(data, ascending=True):
    """Функция сортирует по убыванию по сумме платежа. Второй аргумент необязательный, задает порядок сортировки"""
    return sorted(data, key=lambda x: x.get("Сумма платежа", 0), reverse=ascending)

data = read_excel_file('data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls')
# result = get_sort_dict(data, True)
# print(result)


def get_exchange_rates(currency) -> float:
    """Получаем все курсы валют с сервера API"""
    load_dotenv(".env")
    API_KEY = os.getenv("API_KEY")

    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency}'

    response = requests.get(url)
    data = response.json()
    exchange_rates = data['conversion_rates']["RUB"]

    return exchange_rates

# print(get_exchange_rates("EUR"))