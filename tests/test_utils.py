import os
import json
from unittest.mock import Mock
from unittest.mock import patch
from src.utils import get_transactions_data


@patch("builtins.open")
def test_get_transactions_data_patch(mock_open):

    mock_open.return_value.__enter__.return_value.read.return_value = json.dumps([{"test": "test"}])

    # Проверка на удачную результат. Что в файле список словарей
    assert get_transactions_data("data/operations.json") == [{"test": "test"}]


@patch("builtins.open")
def test_get_transactions_data(open_mock):
    open_mock.return_value.__enter__.return_value.read.return_value = json.dumps([{"test": "test"}])
    os.path.getsize = Mock(return_value=100)
    os.path.exists = Mock(return_value=True)
    assert get_transactions_data("test.json") == [{"test": "test"}]
