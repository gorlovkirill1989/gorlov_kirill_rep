def filter_by_currency(transactions: list, currency: str = "USD") -> int:
    """Функция, которая выдает итератор по заданной валюте"""
    filtered_transactions = list(filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions))
    for transaction in filtered_transactions:
        yield transaction["id"]


def transactions_discriptions(transactions: list) -> str:
    """генератор, который принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_num: int, limit_num: int) -> str:
    """генератор номера карты
    start_num: начальный номер карты
    limit_num: конечный номер карты
    """
    for num in range(start_num, limit_num + 1):
        static_card_num = "0000000000000000"
        str_number = str(num)
        card_number_str = static_card_num[: -len(str_number)] + str_number

        yield f"{card_number_str[:5]} {card_number_str[5:9]} {card_number_str[9:13]} {card_number_str[13:17]}"


if __name__ == "__main__":

    test_card_number_generator = card_number_generator(2311000, 2311999)
    for n in range(10):
        print(next(test_card_number_generator))
