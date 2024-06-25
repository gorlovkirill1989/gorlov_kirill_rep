from unittest.mock import patch

from src.external_api import convert


@patch("requests.get")
def test_convert(mock_get):
    mock_get.return_value.json.return_value = {"result": 100}

    assert convert(amount=2, currency_from="USD") == 100
