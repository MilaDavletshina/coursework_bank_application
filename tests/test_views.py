import datetime
import os
import pytest
import pandas as pd
import unittest
import requests_mock
import os
from pathlib import Path
from src.views import card_operations_info, get_greeting, top_five_transactions, get_currency_rates, get_stocks_prices
from unittest.mock import patch, mock_open
from dotenv import load_dotenv
load_dotenv(".env")
API_KEY = os.getenv("API_KEY")

