from src.masks import mask_acc_number, mask_card_numbers, get_mask_numbers


def test_mask_card_numbers():
    assert mask_card_numbers(7777888811119999) == "7777 88** **** 9999"


def test_mask_acc_number():
    assert mask_acc_number(11112222333344445555) == "**5555"

def test_get_mask_numbers():
    assert get_mask_numbers(7777888811119999) == "7777 88** **** 9999"
    assert get_mask_numbers(11112222333344445555) == "**5555"
    assert get_mask_numbers(111) == "Неправильно введен номер карты/счет. Попробуйте ввести еще раз"





