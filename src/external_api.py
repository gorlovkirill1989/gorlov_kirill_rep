import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

# Отправка GET-запроса к API
# response = requests.get('https://api.github.com/user', headers=headers)


def convert(amount: float, currency_from: str, currency_to: str = "RUB") -> float:
    """метод конвертации из одной валюты в другую с помощью apilayer"""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

    headers = {"apikey": os.getenv("API_KEY")}

    response = requests.get(url, headers=headers)

    return response.json()["result"]
