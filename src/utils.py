import pandas as pd

def read_excel_file(input_file):
    """ Считывание excel файла и преобразование в словарь"""
    df = pd.read_excel(input_file)
    df_dict = df.to_dict(orient="records")
    return df_dict

# input_file = "data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls"
# print(read_excel_file(input_file))

# def read_excel_file(input_file: list) -> list[dict]:
#     """ Считывание excel файла и преобразование в словарь"""
#     data_list = []
#     for transaction in input_file:
#         if pd.notnull(transaction["Номер карты"]):
#             result = {
#                 "Дата операции": transaction["Дата операции"],
#                 "Дата платежа": transaction["Дата платежа"],
#                 "Номер карты": str(transaction["Номер карты"])[-4:],
#                 "Статус": transaction["Статус"],
#                 "Сумма операции": float(transaction["Сумма операции"]),
#                 "Валюта операции": transaction["Валюта операции"],
#                 "Сумма платежа": float(transaction["Сумма платежа"]),
#                 "Валюта платежа": transaction["Валюта платежа"],
#                 "Кэшбэк": float(transaction["Кэшбэк"]),
#                 "Категория": transaction["Категория"],
#                 "MCC": transaction["MCC"],
#                 "Описание": transaction["Описание"],
#                 "Бонусы (включая кэшбэк)": float(transaction["Бонусы (включая кэшбэк)"]),
#                 "Округление на инвесткопилку": float(transaction["Округление на инвесткопилку"]),
#                 "Сумма операции с округлением": float(transaction["Сумма операции с округлением"])
#              }
#             data_list.append(result)
#         else:
#             result = {}
#             data_list.append(result)
#     return data_list
#
# input_file = "data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls"
# print(read_excel_file(input_file))