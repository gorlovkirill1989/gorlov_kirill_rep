from .masks import get_mask_numbers


def mask_bank_data(bank_data: str) -> str:
    data_parts = bank_data.split()

    data_parts[-1] = get_masked_nums(data_parts[-1])

    return " ".join(data_parts)

