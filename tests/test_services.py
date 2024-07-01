import pandas as pd
import os
from unittest.mock import patch
import pytest
from src.services import person_money_transfer


@pytest.fixture
def sample_input_file(tmpdir):
    # Создаем временный файл с данными для тестирования
    sample_data = """
    Дата операции,Статус,Сумма платежа,Категория,Описание
    2024-07-01,Выполнен,100,Перевод,Иванов И.И.
    2024-07-02,Отменен,200,Перевод,Петров П.П.
    """
    file_path = os.path.join(tmpdir, "sample_data.xlsx")
    with open(file_path, "w") as file:
        file.write(sample_data)
    return file_path

def test_person_money_transfer(sample_input_file):
    expected_output = [
        {
            "Дата операции": "2024-07-01",
            "Статус": "Выполнен",
            "Сумма платежа": 100,
            "Категория": "Перевод",
            "Описание": "Иванов И.И."
        }
    ]

    result = person_money_transfer(sample_input_file)
    assert result == json.dumps(expected_output, ensure_ascii=False, indent=4)

def test_person_money_transfer_invalid_file():
    with pytest.raises(ValueError):
        person_money_transfer("invalid_file.xlsx")