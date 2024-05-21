def get_dict_by_key(list_of_dicts: list, state: str = "EXECUTED") -> dict:
    """Функция, которая обходит список словарей и возвращает словарь по ключу"""
    for dictionary in list_of_dicts:
        dictionary.get(state)
        if dictionary["state"] == state:
            return dictionary


def get_dict_by_data(list_of_dicts: list, sort_by_client=True) -> list[dict]:
    """Функция,в котором исходные словари отсортированы по убыванию даты"""
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: x["date"], reverse=sort_by_client)
    return sorted_list_of_dicts
