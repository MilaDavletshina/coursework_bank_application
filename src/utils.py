# Вспомогательные функции, необходимые для работы функции страницы «Главная»
# Функция для страницы «Главная» принимает на вход DataFrame
# используют библиотеку json, используют API, используют библиотеку datetime, logging, pandas

# Вспомогательные функции, необходимые для работы функции страницы «События»,
# отдает корректный JSON-ответ
# используют библиотеку json, используют API, datetime, logging, logging
import pandas as pd

def read_excel_file(input_file):
    """ Считывание excel файла и преобразование в словарь"""
    df = pd.read_excel(input_file)
    df_dict = df.to_dict(orient="records")
    return df_dict

input_file = "data/operations Mon Jan 01 20_45_05 MSK 2024-Mon Jun 24 17_37_09 MSK 2024.xls"
print(read_excel_file(input_file))

