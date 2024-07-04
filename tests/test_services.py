import json
import os

import pytest

from src.services import person_money_transfer


@pytest.fixture
def sample_input_file(tests):
    """Функция создает временный файл для тестирования"""
    sample_data = """
    Дата операции,Статус,Сумма платежа,Категория,Описание
    2024-07-01,Выполнен,100,Перевод,Иванов И.И.
    2024-07-02,Отменен,200,Перевод,Петров П.П.
    """
    file_path = os.path.join(tests, "sample_data.xlsx")
    with open(file_path, "w") as file:
        file.write(sample_data)
    return file_path

def test_person_money_transfer_tmp(sample_input_file):
    """Тест записывает данные во временный файл для тестирования"""
    expected_output = [
    {
        "Дата операции": "2024-07-01",
        "Статус": "Выполнен",
        "Сумма платежа": 100,
        "Категория": "Перевод",
        "Описание": "Иванов И.И.",
    }
    ]
    result = person_money_transfer(sample_input_file)
    assert result == json.dumps(expected_output, ensure_ascii=False, indent=4)



def test_person_money_transfer_invalid_file():
    """Функция тестирования переводы физ.лицу"""
    with pytest.raises(ValueError):
        person_money_transfer("tests/invalid_file.xlsx")


@pytest.mark.parametrize(
    "data, expected",
    [
        ("""
        Дата операции,Статус,Сумма платежа,Категория,Описание
        01.01.2024 20:45:05,OK,600.0,Переводы,Ольга С.
        """,
            {
                "Дата операции": "01.01.2024 20:45:05",
                "Статус": "OK",
                "Сумма платежа": 600.0,
                "Категория": "Переводы",
                "Описание": "Ольга С.",
            }
        )
    ],
)

def test_person_money_transfer_1(data, expected):
    """Тест проверяет перевод физическому лицу"""
    assert person_money_transfer(data) == expected

