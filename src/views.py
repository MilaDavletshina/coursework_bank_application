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

print(greeting())

# как вывести в красивый список, как округлить до двух знаков?
def card_operations_info(transactions):
    """Функция выводит общую информацию по карте"""
    data = pd.read_excel(transactions)

    card_data = {}

    for index, row in data.iterrows():
        card_number = str(row['Номер карты'])[-4:] if pd.notnull(row['Номер карты']) else None
        total_spent = float(row['Сумма операции с округлением'])

        if card_number in card_data:
            card_data[card_number]['total_spent'] += total_spent
        else:
            card_data[card_number] = {
                'last_digits': card_number,
                'total_spent': round(total_spent, 2),
                'cashback': float(total_spent // 100)
            }

    result = [value for value in card_data.values()]

    return result

transactions = 'data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls'
result = card_operations_info(transactions)
print(result)

# "top_transactions": [
#     {
#         "date": "21.12.2021",
#         "amount": 1198.23,
#         "category": "Переводы",
#         "description": "Перевод Кредитная карта. ТП 10.2 RUR"
#     },
#     {
#         "date": "20.12.2021",
#         "amount": 829.00,
#         "category": "Супермаркеты",
#         "description": "Лента"
#     },
#     {
#         "date": "20.12.2021",
#         "amount": 421.00,
#         "category": "Различные товары",
#         "description": "Ozon.ru"
#     },
#     {
#         "date": "16.12.2021",
#         "amount": -14216.42,
#         "category": "ЖКХ",
#         "description": "ЖКУ Квартира"
#     },
#     {
#         "date": "16.12.2021",
#         "amount": 453.00,
#         "category": "Бонусы",
#         "description": "Кешбэк за обычные покупки"
#     }
# ],



def top_transactions(transactions):


transactions = read_excel_file('data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls')
result = top_transactions(transactions)
print(result)
