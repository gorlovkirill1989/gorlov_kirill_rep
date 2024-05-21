def mask_card_numbers(nums: str) -> str:
    """Функция, которая маскирует номер карты"""
    return f"{nums[0:4]} {nums[4:6]}** **** {nums[-4:]}"


def mask_acc_number(nums: str) -> str:
    """Функция, которая маскирует номер счета"""
    return f"**{nums[-4:]}"


def get_mask_numbers(nums: int | str) -> str:
    """Функция, которая проверяет введены ли цифры и карта это, или номер счета"""

    nums = str(nums)

    if len(nums) == 16 and nums.isdigit():
        return mask_card_numbers(nums)

    elif len(nums) == 20 and nums.isdigit():
        return mask_acc_number(nums)

    else:
        return "Неправильно введен номер карты/счет. Попробуйте ввести еще раз"
