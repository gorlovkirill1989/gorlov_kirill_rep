import json
import os
from config import ROOT_DIR


def get_transactions_data(file_path: str = []) -> list:
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    path_to_file = os.path.join(ROOT_DIR, file_path)
    with open(path_to_file, "r", encoding="utf-8") as f:
        json_data_transactions = json.load(f)

        return json_data_transactions

# if __name__ == '__main__':
#     file_path = r"data\operations.json"
#     nnn = get_transactions_data(file_path)
#     print(nnn)



