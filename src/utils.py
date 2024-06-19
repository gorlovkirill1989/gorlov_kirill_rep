import json
import os
from config import ROOT_DIR


def get_transactions_data(file_path: str) -> list[dict]:
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    path_to_file = os.path.join(ROOT_DIR, file_path)

    if os.path.exists(path_to_file) and os.path.getsize(path_to_file) > 0:
        with open(path_to_file, "r", encoding="utf-8") as f:
            json_data_transactions = json.load(f)

            return json_data_transactions
    else:
        return []


if __name__ == "__main__":
    file_path = r"data\operations.json"
    nnn = get_transactions_data("ыавы")
    print(nnn)
