import datetime
import pytest
import pandas as pd
from src.views import card_operations_info, get_greeting, top_five_transactions, get_currency_rates, get_stocks_prices
from unittest.mock import patch, mock_open, Mock

@pytest.fixture
def sample_input_file(tmp_path):
    data = {
        "Номер карты": [*7371, None],
        "Сумма операции с округлением": [500.0, 150.0],
    }
    df = pd.DataFrame(data)
    file_path = tmp_path / "sample_input_file.xlsx"
    df.to_excel(file_path, index=False)
    return str(file_path)

def test_card_operations_info(sample_input_file):
    """"Тест на проверку информации по карте"""
    expected_output = {
        "cards": [
            {
                "last_digits": "*7371",
                "total_spent": 500.0,
                "cashback": 5.0,
            },
            {
                "last_digits": None,
                "total_spent": 150.0,
                "cashback": 1.5,
            },
        ]
    }
    assert card_operations_info(sample_input_file) == expected_output

def test_card_operations_info_with_invalid_file(tmp_path):
    invalid_file_path = tmp_path / "invalid_file.xlsx"
    invalid_file_path.write_text("invalid file content")
    assert card_operations_info(invalid_file_path) == {}

@pytest.mark.parametrize(
    "date, expected",
    [(datetime.datetime.now(), datetime.datetime.now())])

def test_get_greeting(date: str, expected: str) -> None:
    """Тест на проверку текущего времени"""
    assert 'Доброе утро!' == get_greeting()


def test_top_five_transactions(mocker):
    "Тест на функцию топ-5 транзакций"
    data = {
        "Дата платежа": "30.05.2024 23:26:03",
        "Сумма платежа": 500.0,
        "Категория": "Переводы",
        "Описание": "Ekaterina P."
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
    data = 'invalid_json_data'
    with patch("builtins.open", mock_open(read_data=data)):
        result = get_currency_rates("test_file.json")
        assert result == []

def test_get_stocks_prices_invalid_format():
    data = 'invalid_json_data'
    with patch("builtins.open", mock_open(read_data=data)):
        result = get_stocks_prices("test_file.json")
        assert result == []
