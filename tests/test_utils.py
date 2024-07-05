import os

from unittest.mock import patch


from dotenv import load_dotenv

from src.utils import get_exchange_rates, get_stock_api_price

API_KEY = os.getenv("API_KEY_STOCK")
API_KEY_STOCK = os.getenv("API_KEY_STOCK")
load_dotenv(".env")
input_file = os.getenv("INPUT_FILE")


def test_get_exchange_rates_valid():
    """Проверяет на формат строки с плавающей точкой"""
    currency = "USD"
    price = get_exchange_rates(currency)
    assert type(price) is float


def test_get_exchange_rates_invalid():
    """Проверяет несуществующую валюту"""
    currency = "INVALID"
    price = get_stock_api_price(currency)
    assert price == 0.0


@patch("requests.get")
def test_get_stock_api_price(mock_get):
    """Тест проверяет получение стоимости акции"""
    mock_get.return_value.json.return_value = {
        "Global Quote": {
            "01. symbol": "IBM",
            "02. open": "173.4500",
            "03. high": "176.4600",
            "04. low": "173.3800",
            "05. price": "175.1",
            "06. volume": "3320961",
            "07. latest trading day": "2024-07-01",
            "08. previous close": "172.9500",
            "09. change": "2.1500",
            "10. change percent": "1.2431%",
        }
    }
    assert get_stock_api_price("IBM") == 0.0
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={API_KEY_STOCK}"
    mock_get.assert_called_once_with(url)


def test_get_stock_api_price_valid():
    """Тест проверяет формат получения цены"""
    stock = "AAPL"
    price = get_stock_api_price(stock)
    assert type(price) is float


def test_get_stock_api_price_invalid():
    stock = "INVALID"
    price = get_stock_api_price(stock)
    assert price == 0.0


def test_get_exchange_rates_1():
    """Тест ппроверяет на ошибку получения данных с сервера"""
    assert get_exchange_rates("EUR") == 0.0
