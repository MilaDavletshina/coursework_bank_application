import json
import os
import pytest

from unittest.mock import patch
from dotenv import load_dotenv
from src.utils import get_exchange_rates, get_stock_api_price


load_dotenv(".env")
API_KEY = os.getenv("API_KEY")

@patch("requests.get")
def test_get_exchange_rates(mock_get):
    mock_get.return_value.text = json.dumps(
        {
            "result": "success",
			"documentation": "https://www.exchangerate-api.com/docs",
			"terms_of_use": "https://www.exchangerate-api.com/terms",
			"time_last_update_unix": 1585267200,
			"time_last_update_utc": "Fri, 27 Mar 2020 00:00:00 +0000",
			"time_next_update_unix": 1585353700,
			"time_next_update_utc": "Sat, 28 Mar 2020 00:00:00 +0000",
			"base_code": "USD",
			"conversion_rates": {
				"USD": 1,
				"RUB": 85.6933
			}
        }
    )

    assert get_exchange_rates("USD") == 85.6933
    mock_get.assert_called_once_with(
        "https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    )

def test_get_stock_api_price():
	with patch('my_module.requests.get') as mock_get:
		mock_get.return_value.json.return_value = {
			"Global Quote": {
			"05. price": "100.00"
			}
		}
		assert get_stock_api_price("AAPL") == "100.00"

	with patch('my_module.requests.get') as mock_get:
		mock_get.side_effect = ValueError
		assert get_stock_api_price("AAPL") == "Ошибка загрузки. Проверьте введенные данные."
