import pytest
import pandas as pd
import json
import os
from unittest.mock import patch
from src.services import person_money_transfer

# Путь к тестовым файлам
TEST_FILE_PATH = 'test_file.xlsx'

def create_test_file(data):
    """Создание тестового файла"""
    df = pd.DataFrame(data)
    df.to_excel(TEST_FILE_PATH, index=False)

def test_successful_transfer():
    """Тест проверяет успешное выполнение функции"""
    data = {
        "Дата операции": ["2024-01-01", "2024-01-02"],
        "Статус": ["OK", "OK"],
        "Сумма платежа": [100, 200],
        "Категория": ["Переводы", "Переводы"],
        "Описание": ["Ольга С.", "Катя П."]
    }
    create_test_file(data)

    result = person_money_transfer(TEST_FILE_PATH)
    expected = [
        {
            "Дата операции": "2024-01-01",
            "Статус": "OK",
            "Сумма платежа": 100,
            "Категория": "Переводы",
            "Описание": "Ольга С."
        },
        {
            "Дата операции": "2024-01-02",
            "Статус": "OK",
            "Сумма платежа": 200,
            "Категория": "Переводы",
            "Описание": "Катя П."
        }
    ]
    assert json.loads(result) == expected

def test_no_transfers():
    """Тест на отсутствие перевода"""
    data = {
        "Дата операции": ["2024-01-01", "2024-01-02"],
        "Статус": ["OK", "OK"],
        "Сумма платежа": [100, 200],
        "Категория": ["Переводы", "Переводы"],
        "Описание": ["ФИО_1", "ФИО_2"]
    }
    create_test_file(data)

    result = person_money_transfer(TEST_FILE_PATH)
    assert result == json.dumps([], ensure_ascii=False, indent=4)

def remove_module():
    """Удаление тестового файла"""
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)


def test_person_money_transfer_invalid_file():
    """Функция тестирования ошибки файла"""
    with pytest.raises(ValueError):
        person_money_transfer("tests/invalid_file.xlsx")