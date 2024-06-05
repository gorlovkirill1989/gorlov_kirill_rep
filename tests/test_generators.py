import pytest
from src.generators import filter_by_currency, transactions_discriptions, card_number_generator


def test_filter_by_currency(bank_operations):
    generator_filter_by_currency = filter_by_currency(bank_operations)
    assert next(generator_filter_by_currency) == 939719570
    assert next(generator_filter_by_currency) == 142264268
    assert next(generator_filter_by_currency) == 895315941


def test_transactions_discriptions(bank_operations):
    generator_transactions_discriptions = transactions_discriptions(bank_operations)
    assert next(generator_transactions_discriptions) == "Перевод организации"
    assert next(generator_transactions_discriptions) == "Перевод со счета на счет"
    assert next(generator_transactions_discriptions) == "Перевод со счета на счет"


def test_card_number_generator():
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"

