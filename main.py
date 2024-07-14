import os

from config import ROOT_DIR
from src.utils import filter_transactions2, get_transactions_data
from src.widget import get_clear_data, mask_bank_data


def get_user_input(description: str = "", fail: str = "", options: list[str] = ()) -> str:
    while True:
        value = input(f"{description}\n>>> ").lower()

        if not options:
            return value

        if value not in options:
            print(fail)
            continue

        return value


def get_bool_user_input(description: str = "", options: tuple[str, str] = ("", "")) -> bool:
    fail = "Нет такого варианта меню. Введите пункт меню заново"
    # return get_user_input(description=description, options=list(options), fail=fail) == options[0]
    return get_user_input(description=description, options=["1", "2"], fail=fail) == "1"


def main():
    files_map = {"1": "operations.json", "2": "transactions_excel.xlsx", "3": "transactions.csv"}
    ext_map = {"1": "JSON", "2": "CSV", "3": "XLSX"}

    value = get_user_input(
        description="""
Привет! 
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""",
        fail="Нет такого варианта меню. Введите пункт меню заново",
        options=["1", "2", "3"],
    )

    print(f"Для обработки выбран {ext_map[value]}-файл.")

    path_to_file = os.path.join(ROOT_DIR, "data", files_map[value])

    transactions = get_transactions_data(path_to_file)

    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    status = ""

    print("Введите статус, по которому необходимо выполнить фильтрацию.\n")

    while True:
        value = input(f'Доступные для фильтровки статусы: {", ".join(statuses)}\n>>> ')

        if value.upper() not in statuses:
            print(f'Статус операции "{value}" не доступен.\n')
            continue

        status = value.upper()
        break

    print(status)

    transactions = filter_transactions2(transactions, status, "state")

    default_tuple = ("1", "2")

    is_sort_by_date = get_bool_user_input("Отсортировать операции по дате? \n1. Да\n2. Нет", default_tuple)

    if is_sort_by_date:
        order_by_asc_desc = get_bool_user_input("Отсортировать по \n1. возрастанию \n2. по убыванию?", ("1", "2"))

        for transaction in transactions:
            if transaction.get("date", "") != "":
                transactions.sort(key=lambda x: x.get("date", ""), reverse=not order_by_asc_desc)

    is_rub_only = get_bool_user_input("Выводить только рублевые тразакции? \n1. Да\n2. Нет", default_tuple)

    is_filter_by_word = get_bool_user_input(
        "Отфильтровать список транзакций по определенному слову в описании? \n1. Да\n2. Нет", default_tuple
    )

    if is_filter_by_word:
        word = input('Введите слово, например "Перевод"\n>>> ')
        transactions = filter_transactions2(transactions, word)

    if is_rub_only:
        transactions = list(
            filter(lambda x: x.get("operationAmount", {}).get("currency", {}).get("code", "") == "RUB", transactions)
        )

    if not transactions:
        print("Ничего не найдено...\n")

    else:
        print("Распечатываю итоговый список транзакций...\n")

        for tr in transactions:
            if tr.get("from", 0) != 0 and tr.get("to", 0) != 0:
                print(f"{get_clear_data(tr["date"])} {tr["description"]}")
                print(f"{mask_bank_data(tr.get("from"))} -> {mask_bank_data(tr.get("to"))}\n")


if __name__ == "__main__":
    main()
