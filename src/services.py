import re
import json
import pandas as pd
import os
import datetime
from dotenv import load_dotenv
from log import setup_logger

load_dotenv(".env")
input_file = os.getenv("INPUT_FILE")

logger = setup_logger(datetime.datetime.now().strftime("%Y-%m-%d"))
def person_money_transfer(input_file):
    """Функция выводит переводы физическим лицам"""
    transfers = []
    pattern = r'(\w+\s\w\.)'
    data = pd.read_excel(input_file)

    try:
        for index, row in data.iterrows():
            description = row["Описание"]
            if re.search(pattern, description):
                transfer = {
                    "Дата операции": row["Дата операции"],
                    "Дата платежа": row["Дата платежа"],
                    "Номер карты": row["Номер карты"],
                    "Статус": row["Статус"],
                    "Сумма операции": row["Сумма операции"],
                    "Валюта операции": row["Валюта операции"],
                    "Сумма платежа": row["Сумма платежа"],
                    "Валюта платежа": row["Валюта платежа"],
                    "Кэшбэк": row["Кэшбэк"],
                    "Категория": row["Категория"],
                    "MCC": row["MCC"],
                    "Описание": description,
                    "Бонусы (включая кэшбэк)": row["Бонусы (включая кэшбэк)"],
                    "Округление на инвесткопилку": row["Округление на инвесткопилку"],
                    "Сумма операции с округлением": row["Сумма операции с округлением"]
                }
                transfers.append(transfer)
                logger.info(f"функция {person_money_transfer} успешно реализована")

                return json.dumps(transfers, ensure_ascii=False, indent=4)
    except ValueError:
        logger.error("Проверьте формат загруженного файла!")
        return []

# print(person_money_transfer(input_file))


