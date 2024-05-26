from src.widget import get_clear_data, mask_bank_data


def test_get_clear_data():
    assert get_clear_data("2018-07-11T02:26:18.671407") == "11.07.2018"


def test_mask_bank_data(): #Maestro 1596837868705199 Visa Classic 6831982476737658
    assert mask_bank_data("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_bank_data("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"