from typing import Generator


def filter_by_currency(transactions: list, currency: str = "USD") -> "Generator":
    """Функция, которая выдает итератор по заданной валюте"""
    filtered_transactions = list(filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions))
    for transaction in filtered_transactions:
        yield transaction["id"]


def transactions_discriptions(transactions: list) -> "Generator":
    """генератор, который принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_num: int, limit_num: int) -> "Generator":
    """генератор номера карты
    start_num: начальный номер карты
    limit_num: конечный номер карты
    """
    for num in range(start_num, limit_num + 1):
        static_card_num = "0000000000000000"
        str_number = str(num)
        card_number_str = static_card_num[: -len(str_number)] + str_number

        yield f"{card_number_str[:4]} {card_number_str[4:8]} {card_number_str[8:12]} {card_number_str[12:]}"
