def get_dict_by_key(list_of_dicts: list, state: str = "EXECUTED") -> dict:
    """Функция, которая обходит список словарей и возвращает словарь по ключу"""
    new_dict_list = []
    for dictionary in list_of_dicts:
        if dictionary.get("state") == state:
            new_dict_list.append(dictionary)
    return new_dict_list


def get_dict_by_data(list_of_dicts: list, sort_by_client=True) -> list[dict]:
    """Функция,в котором исходные словари отсортированы по убыванию даты"""
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: x["date"], reverse=sort_by_client)
    return sorted_list_of_dicts


if __name__ == "__main__":
    print(
        get_dict_by_data(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
        )
    )
