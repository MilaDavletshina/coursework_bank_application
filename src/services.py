import re
import json
import pandas as pd
import os
import datetime
from dotenv import load_dotenv
from src.log import setup_logger

load_dotenv(".env")
input_file = os.getenv("INPUT_FILE")

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_log = os.path.join(current_dir, "../logs", "services.log")
logger = setup_logger("services", file_path_log)
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
                    "Статус": row["Статус"],
                    "Сумма платежа": row["Сумма платежа"],
                    "Категория": row["Категория"],
                    "Описание": description
                }
                transfers.append(transfer)
                logger.info(f"функция {person_money_transfer} успешно реализована")

        return json.dumps(transfers, ensure_ascii=False, indent=4)
    except ValueError:
        logger.error("Проверьте формат загруженного файла!")
        return []

# print(person_money_transfer(input_file))


