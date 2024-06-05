from src.processing import get_dict_by_data, get_dict_by_key
from src.widget import get_clear_data, mask_bank_data
from src.masks import mask_acc_number, mask_card_numbers, get_mask_numbers
from src.decorators import log

if __name__ == "__main__":

    @log()
    def add_numbers(x, y):
        return x / y

    add_numbers(3, 0)

    def hi_wrapper():
        def hi():
            print("hopijertoijret!")

        return hi
