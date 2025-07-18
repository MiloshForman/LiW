from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_name: str='0') -> str:
    """Принимает тип-номер карты или счета card_name и возвращает замаскированный номер card_mask"""

    card_word = ""
    card_number = ""
    card_mask = ""

    if card_name == None:
        card_name = '0'

    for card_symbol in card_name:
        if card_symbol.isdigit():
            card_number += card_symbol
        else:
            card_word += card_symbol

    if len(card_number) == 16:
        card_mask = card_word + get_mask_card_number(int(card_number))

    elif len(card_number) == 20:
        card_mask = card_word + get_mask_account(int(card_number))

    else:
        return 'Неправильный номер'

    return card_mask


def get_date(long_date: str) -> str:
    """принимает на вход строку с датой long_date и отдает корректный результат в формате 'ДД.ММ.ГГГГ'"""

    return f"{long_date[8:10]}-{long_date[5:7]}-{long_date[:4]}"
