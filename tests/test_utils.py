import json
from unittest.mock import patch

from src.utils import get_transaction_amount, get_transactions_data


@patch("builtins.open")
def test_get_transactions_data_patch(mock_open):
    mock_open.return_value.__enter__.return_value.read.return_value = json.dumps([{"test": "test"}])

    # Проверка на удачную результат. Что в файле список словарей
    assert get_transactions_data("data/operations.json") == [{"test": "test"}]


@patch("builtins.open")
def test_get_transactions_data(open_mock):
    open_mock.return_value.__enter__.return_value.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions_data("test.json") == [{"test": "test"}]

    open_mock.return_value.__enter__.return_value.read.return_value = json.dumps({"test": "test"})
    assert get_transactions_data("test.json") == []

    open_mock.return_value.__enter__.return_value.read.return_value = "bla-bla-bla"
    assert get_transactions_data("test.json") == []


@patch("src.utils.convert")
def test_get_transaction_amount(mock_convert):
    mock_convert.return_value = 100

    transaction_1 = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "1", "currency": {"name": "USD", "code": "USD"}},
    }

    transaction_2 = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "10", "currency": {"name": "RUB", "code": "RUB"}},
    }
    assert get_transaction_amount(transaction_1) == 100
    assert get_transaction_amount(transaction_2) == 10
