import pandas as pd
from datetime import datetime, timedelta
from src.reports import spending_by_category

def test_spending_by_category_no_date():
    transactions = pd.DataFrame({
        'Дата операции': ['2024-06-20 17:53:01', '2024-06-18 17:25:15', '2024-06-11 09:55:02'],
        'Сумма операции': [-416.57, -158.00, -259.98],
        'Категория': ['Супермаркеты', 'Супермаркеты', 'Супермаркеты']
    })

    result = spending_by_category(transactions, 'Супермаркеты')
    assert len(result) == 3

def test_spending_by_category_with_date():
    transactions = pd.DataFrame({
        'Дата операции': ['2024-06-20 17:53:01', '2024--18 17:25:15', '2024-06-11 09:55:02'],
        'Сумма операции': [-416.57, -158.00, -259.98],
        'Категория': ['Супермаркеты', 'Супермаркеты', 'Супермаркеты']
    })

    result = spending_by_category(transactions, 'Супермаркеты', '01.06.2024')
    assert len(result) == 0