import re
import json
import pandas as pd


def person_money_transfer(input_file):
    transfers = []
    pattern = r'(\w+\s\w\.)'
    data = pd.read_excel(input_file)

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

    return json.dumps(transfers, ensure_ascii=False, indent=4)

input_file = 'data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls'
print(person_money_transfer(input_file))


