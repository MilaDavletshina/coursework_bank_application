import logging
import os
from dotenv import load_dotenv

load_dotenv(".env")
LOGS_REPORT = os.getenv("LOGS_REPORT")

def setup_logger(name: str) -> logging.Logger:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filemode="w")
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(os.path.join(LOGS_REPORT, f"{name}.log"), mode="w")
    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger



