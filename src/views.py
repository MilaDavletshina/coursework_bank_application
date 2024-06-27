import datetime
import pandas as pd


def greeting():
    """Функция приветствия в зависимости от времени суток"""
    now = datetime.datetime.now()
    if now.hour > 6 and now.hour <= 12 :
        return "Доброе утро"
    if now.hour > 12 and now.hour <= 18 :
        return "Добрый день"
    if now.hour > 18 and now.hour <= 24 :
        return "Добрый вечер"
    if now.hour >= 0 and now.hour <= 6 :
        return "Добрый ночи"
print(greeting())


def card_operations_info(transactions):
    """Функция выводит общую информацию по карте"""
    data = pd.read_excel(transactions)

    card_data = {}

    for index, row in data.iterrows():
        card_number = str(row['Номер карты'])[-4:] if pd.notnull(row['Номер карты']) else None
        total_spent = row['Сумма операции с округлением']

        if card_number in card_data:
            card_data[card_number]['total_spent'] += total_spent
        else:
            card_data[card_number] = {
                'last_digits': card_number,
                'total_spent': total_spent,
                'cashback': total_spent // 100
            }

    result = [value for value in card_data.values()]

    return result

transactions = 'data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls'
result = card_operations_info(transactions)
print(result)


