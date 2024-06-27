import datetime
import pandas as pd


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

# "currency_rates": [
#     {
#       "currency": "USD",
#       "rate": 73.21
#     },
#     {
#       "currency": "EUR",
#       "rate": 87.08
#     }
#   ],