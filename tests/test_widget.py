import pytest
from src.widget import get_clear_data, mask_bank_data


@pytest.mark.parametrize("date, expected_result", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("2019-08-12T03:22:18.671407", "12.08.2019"),
    ("2019-07-12T02:26:18.671407", "12.07.2019"),
    ("2020-08-12T03:22:18.671407", "12.08.2020"),
])

def test_get_clear_date(date, expected_result):
    assert get_clear_data(date) == expected_result


@pytest.mark.parametrize("bank_data, expected_result", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305")
])

def test_mask_bank_data(bank_data, expected_result):
    assert mask_bank_data(bank_data) == expected_result