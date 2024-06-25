import pytest

from src.masks import get_mask_numbers, mask_acc_number, mask_card_numbers


@pytest.mark.parametrize(
    "nums, expected_result",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (7000792289606362, "7000 79** **** 6362"),
        (7200792289606361, "7200 79** **** 6361"),
        (7100792289606362, "7100 79** **** 6362"),
    ],
)
def test_mask_card_numbers(nums, expected_result):
    assert mask_card_numbers(nums) == expected_result


@pytest.mark.parametrize(
    "nums, expected_result",
    [
        (12345678901234567890, "**7890"),
        (12345678901234567891, "**7891"),
        (12345678901234567892, "**7892"),
        (12345678901234567893, "**7893"),
    ],
)
def test_mask_acc_number(nums, expected_result):
    assert mask_acc_number(nums) == expected_result


@pytest.mark.parametrize(
    "card_or_acc_nums, expected_result",
    [
        (12345678901234567890, "**7890"),
        (7000792289606362, "7000 79** **** 6362"),
        (123, "Неправильно введен номер карты/счет. Попробуйте ввести еще раз"),
        ("буквы", "Неправильно введен номер карты/счет. Попробуйте ввести еще раз"),
    ],
)
def test_get_mask_numbers(card_or_acc_nums, expected_result):
    assert get_mask_numbers(card_or_acc_nums) == expected_result
