from src.processing import get_dict_by_data, get_dict_by_key
from src.widget import get_clear_data, mask_bank_data
from src.masks import mask_acc_number, mask_card_numbers, get_mask_numbers

if __name__ == "__main__":
    print(mask_card_numbers(7777888811119999))

    print(mask_acc_number(11112222333344445555))

    print(
        get_dict_by_key(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        )
    )
    print(mask_bank_data("Visa Platinum 7000792289606361"))


