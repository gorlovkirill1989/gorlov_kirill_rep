# Проект "Приложение для банка"

## Описание:

Проект "Приложение для банка" - нихрена не понятно, но очень интересно

Функции:

`mask_card_numbers` - Функция, которая маскирует номер карты

`mask_acc_number` - Функция, которая маскирует номер счета

`get_mask_numbers` - Функция, которая проверяет введены ли цифры и карта это, или номер счета

`get_clear_data` - Функция, которая получает дату со временем и возвращает дату

`mask_bank_data` - Функция, которая отделяет название карты и счета от номера

`get_dict_by_key` - Функция, которая обходит список словарей и возвращает словарь по ключу

`get_dict_by_data` Функция,в котором исходные словари отсортированы по убыванию даты

`filter_by_currency` Функция, которая выдает итератор по заданной валюте

Генераторы:
`filter_by_currency` Функция, которая выдает итератор по заданной валюте

`transactions_discriptions` генератор, который принимает список словарей и возвращает описание каждой операции по очереди

`card_number_generator` генератор номера карты


#
## Пакет `tests`:
#### test_masks.py - тестирование функций: `mask_card_numbers`, `mask_acc_number`, `get_mask_numbers`

#### test_widget.py - тестирование функций: `get_clear_data`, `mask_bank_data`

#### test_processing.py - тестирование функций: `get_dict_by_key`, `get_dict_by_data`

#### test_generators - тестирование функций/генераторов: `filter_by_currency`, `transactions_discriptions`, `card_number_generator`

#### conftest.py - фикстуры (тестовые данные) 



1. Клонируйте репозиторий:
```
git clone https://github.com/gorlovkirill1989/gorlov_kirill_rep.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

## тестирование:

тестирование можно сделать командой `pytest` 
