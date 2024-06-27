from src.logger import create_logger

logger = create_logger("masks")


def mask_card_numbers(nums: str | int) -> str:
    """Функция, которая маскирует номер карты"""
    nums = str(nums)
    logger.info(f"замаскирован номер карты {nums}")
    return f"{nums[0:4]} {nums[4:6]}** **** {nums[-4:]}"


def mask_acc_number(nums: str) -> str:
    """Функция, которая маскирует номер счета"""
    nums = str(nums)
    logger.info(f"замаскирован номер счета {nums}")
    return f"**{nums[-4:]}"


def get_mask_numbers(nums: int | str) -> str:
    """Функция, которая проверяет введены ли цифры и карта это, или номер счета"""

    nums = str(nums)

    if len(nums) == 16 and nums.isdigit():
        logger.info(f"Передана карта {nums}")
        return mask_card_numbers(nums)

    elif len(nums) == 20 and nums.isdigit():
        logger.info(f"Передан счёт {nums}")
        return mask_acc_number(nums)

    else:
        logger.info(f"Неправильно введен номер карты/счет {nums}")
        return "Неправильно введен номер карты/счет. Попробуйте ввести еще раз"


if __name__ == "__main__":
    get_mask_numbers(111111111111111)
