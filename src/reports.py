import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from src.log import setup_logger


load_dotenv(".env")
input_file = os.getenv("INPUT_FILE")

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_log = os.path.join(current_dir, "../logs", "reports.log")
logger = setup_logger("reports", file_path_log)


def write_to_file(file_name: str = 'report.txt'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                with open(file_name, 'w') as file:
                    file.write(str(result))
                return result
                    # file.write(result.to_string(index=False))
                    # print(result)

            except Exception as e:
                with open(file_name, 'w') as file:
                    file.write(f"result.to_string(index=False): {type(e).__name__}. Inputs {args}, {kwargs}")
                    print(f"file.write(result.to_string(index=False): {type(e).__name__}. Inputs {args}, {kwargs}")
                return []
        return wrapper
    return decorator

@write_to_file('spending_by_category_report.txt')
def spending_by_category(transactions, category, date=None, file=None) -> pd.DataFrame:
    """Функция формирует отчет "траты по категориям" по заданной пользователем категории,
    в период за 3 месяца от указанной пользователем даты. Если дата отсутствует, то берется текущая дата """

    if date is None:
        date = datetime.now()
        logger.info(f"Дата ввода отсутствует. Отчет формируется от {date} даты")
    else:
        date = datetime.strptime(date, '%d.%m.%Y')
    print(date)
    three_months_ago = date - timedelta(days=90)

    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'])

    filtered_transactions = transactions[(transactions['Дата операции'] >= three_months_ago) & (transactions['Категория'] == category)]

    filtered_transactions['Дата операции'] = filtered_transactions['Дата операции'].dt.strftime('%d.%m.%Y %H:%M:%S')
    output = filtered_transactions[['Дата операции', 'Сумма операции', 'Категория']]

    if file:
        file.write(str(output))

    return output


# transactions = pd.read_excel(input_file)
# category = "Супермаркеты"
# date = '01.01.2024'
#
# result = spending_by_category(transactions, category)
# print(result)