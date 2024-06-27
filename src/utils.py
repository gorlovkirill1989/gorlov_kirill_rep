import json
import os

import pandas as pd

from config import ROOT_DIR
from src.external_api import convert
from src.logger import create_logger

logger = create_logger("utils")


def get_transactions_data(file_path: str) -> list[dict]:
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях"""

    # записываем путь до до файла и забираем расширение указывая индекс [-1]
    file_extension = os.path.splitext(file_path)[-1]

    try:
        if file_extension == ".csv":
            file_data = pd.read_csv(file_path, delimiter=";", encoding="utf8")

            # преобразуем в список словарей
            data_frame_file_data = file_data.to_dict("records")

            logger.info("содержимое файла csv успешно передано")
            return data_frame_file_data

        elif file_extension == ".xlsx":
            file_data = pd.read_excel(file_path)

            # преобразуем в список словарей
            data_frame_file_data = file_data.to_dict("records")

            logger.info("содержимое файла xlsx успешно передано")
            return data_frame_file_data

        else:

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
    # path_to_file = os.path.join(ROOT_DIR, "data", "transactions.csv")
    path_to_file = os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx")

    operations = get_transactions_data(path_to_file)
    print(operations)
