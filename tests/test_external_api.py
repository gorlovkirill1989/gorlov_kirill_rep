from unittest.mock import patch
from src.external_api import convert, get_transaction_amount


@patch("requests.get")
def test_convert(mock_get):
    mock_get.return_value.json.return_value = {"result": 100}

    assert convert(amount=2, currency_from="USD") == 100


@patch("src.external_api.convert")
def test_get_transaction_amount(mock_convert):
    transaction_1 = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "10", "currency": {"name": "USD", "code": "USD"}},
    }
    transaction_2 = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "10", "currency": {"name": "RUB", "code": "RUB"}},
    }

    mock_convert.return_value = 880

    assert get_transaction_amount(transaction_1) == 880
    assert get_transaction_amount(transaction_2) == 10
