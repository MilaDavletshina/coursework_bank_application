import pytest
# from unittest.mock import patch, MagicMock
from src.utils import get_stock_api_price

def test_get_stock_api_price_valid():
    stock = "AAPL"
    price = get_stock_api_price(stock)
    assert type(price) == float

def test_get_stock_api_price_invalid():
    stock = "INVALID"
    price = get_stock_api_price(stock)
    assert price == 0.0

def test_get_stock_api_price_exception():
    stock = ""
    price = get_stock_api_price(stock)
    assert price == "Ошибка загрузки. Проверьте введенные данные."