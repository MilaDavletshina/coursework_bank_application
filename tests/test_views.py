from unittest.mock import mock_open, patch

import pandas as pd
import pytest
from freezegun import freeze_time

from src.views import (
    card_operations_info,
    get_currency_rates,
    get_greeting,
    top_five_transactions,
)


@pytest.fixture
def sample_input_file(tmp_path):
    data = {
        "Номер карты": ["123456789", "987654321"],
        "Сумма операции с округлением": [500.00, 150.00],
    }
    df = pd.DataFrame(data)
    file_path = tmp_path / "sample_input_file.xlsx"
    df.to_excel(file_path, index=False)
    return str(file_path)


def test_card_operations_info(sample_input_file):
    """ "Тест на проверку информации по карте"""
    expected_output = {
        "cards": [
            {
                "last_digits": "6789",
                "total_spent": 500.00,
                "cashback": 5.0,
            },
            {
                "last_digits": "4321",
                "total_spent": 150.00,
                "cashback": 1.5,
            },
        ]
    }
    assert card_operations_info(sample_input_file) == expected_output


@freeze_time("2023-10-01 08:00:00")
def test_greeting_morning():
    assert get_greeting() == "Доброе утро!"


@freeze_time("2023-10-01 13:00:00")
def test_greeting_afternoon():
    assert get_greeting() == "Добрый день!"


@freeze_time("2023-10-01 19:00:00")
def test_greeting_evening():
    assert get_greeting() == "Добрый вечер!"


@freeze_time("2023-10-01 03:00:00")
def test_greeting_night():
    assert get_greeting() == "Доброй ночи!"


def test_top_five_transactions(mocker):
    "Тест на функцию топ-5 транзакций"
    data = {
        "Дата платежа": "30.05.2024 23:26:03",
        "Сумма платежа": 500.0,
        "Категория": "Переводы",
        "Описание": "Ekaterina P.",
    }
    df = pd.DataFrame([data])

    mocker.patch("pandas.read_excel", return_value=df)

    result = top_five_transactions("test.xlsx")

    assert "top_transactions" in result
    assert len(result["top_transactions"]) == 1
    assert result["top_transactions"][0]["date"] == data["Дата платежа"]
    assert result["top_transactions"][0]["amount"] == data["Сумма платежа"]
    assert result["top_transactions"][0]["category"] == data["Категория"]
    assert result["top_transactions"][0]["description"] == data["Описание"]


def test_get_currency_rates_invalid_format():
    data = "invalid_json_data"
    with patch("builtins.open", mock_open(read_data=data)):
        result = get_currency_rates("test_file.json")
        assert result == []
