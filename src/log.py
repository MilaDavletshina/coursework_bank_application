import logging
import os
from dotenv import load_dotenv

load_dotenv(".env")
# LOGS_REPORT = os.getenv("LOGS_REPORT")

def setup_logger(name: str, file_logs: str):
    """Функция логирования"""
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(file_logs, mode="w")
    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger




