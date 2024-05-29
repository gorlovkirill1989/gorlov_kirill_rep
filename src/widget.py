from src.masks import get_mask_numbers


def get_clear_data(data_time: str) -> str:
    """Функция, которая получает дату со временем и возвращает дату"""
    new_data_list = data_time.split("T")
    data = new_data_list[0].split("-")

    return f"{data[-1]}.{data[-2]}.{data[-3]}"


def mask_bank_data(bank_data: str) -> str:
    """Функция, которая отделяет название карты и счета от номера"""

    data_parts = bank_data.split()
    data_parts[-1] = get_mask_numbers(data_parts[-1])

    return " ".join(data_parts)


if __name__ == "__main__":
    print(mask_bank_data("Maestro 1596837868705199"))
    print(mask_bank_data("Visa Classic 6831982476737658"))
    print(get_clear_data("2018-07-11T02:26:18.671407"))
