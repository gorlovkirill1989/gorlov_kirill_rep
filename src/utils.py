import json
import os

from config import ROOT_DIR
from src.external_api import convert
from src.logger import create_logger

logger = create_logger("utils")


def get_transactions_data(file_path: str) -> list[dict]:
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            json_data_transactions = json.load(file)

            # Проверяем, является ли содержимое списком
            if not isinstance(json_data_transactions, list):
                return []
                logger.info("содержимое файла JSON не является списком")
            logger.info("содержимое файла JSON успешно передано")
            return json_data_transactions

    except json.JSONDecodeError:
        # Если файл не JSON
        logger.info("Формат файла не JSON")
        return []

    except FileNotFoundError:
        logger.info("файл JSON не найден")
        return []


def get_transaction_amount(transaction: dict) -> float:
    """функциz, которая возвращает сумму транзакции в рублях, если валюта задана в другой валюте"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        logger.info("Сумма транзакции передана в RUB")
        return amount

    logger.info(f"Сумма транзакции передана в {currency}")
    return convert(amount, currency)


if __name__ == "__main__":

    path_to_file = os.path.join(ROOT_DIR, "data", "operations.json")

    operations = get_transactions_data(path_to_file)

