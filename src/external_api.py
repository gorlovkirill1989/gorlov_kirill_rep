import os
from dotenv import load_dotenv
import requests

# Загрузка переменных из .env-файла
load_dotenv()

# Отправка GET-запроса к API
# response = requests.get('https://api.github.com/user', headers=headers)


def convert(amount: float, currency_from: str, currency_to: str = "RUB") -> float:
    """метод конвертации из одной валюты в другую с помощью apilayer"""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

    headers = {"apikey": os.getenv("API_KEY")}

    response = requests.get(url, headers=headers)

    print(response.json())

    return response.json()["result"]


def get_transaction_amount(transaction: dict) -> float:
    """функциz, которая возвращает сумму транзакции в рублях, если валюта задана в другой валюте"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    return convert(amount, currency)


if __name__ == "__main__":

    print(
        get_transaction_amount(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "1", "currency": {"name": "USD", "code": "USD"}},
            }
        )
    )
