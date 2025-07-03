from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(card_name: str) -> str:
    """Принимает тип-номер карты или счета
       Возвращает замаскированный номер"""

    card_word = ""
    card_number = ""
    card_mask = ""

    for card_symbol in card_name:
        if card_symbol.isdigit():
            card_number += card_symbol
        else:
            card_word += card_symbol

    if len(card_number) == 16:
        card_mask = card_word + get_mask_card_number(int(card_number))

    if len(card_number) == 20:
        card_mask = card_word + get_mask_account(int(card_number))

    return card_mask


def get_date(long_date):
    """принимает на вход строку и отдает корректный результат в формате 'ДД.ММ.ГГГГ'"""

    return f"{long_date[8:10]}-{long_date[5:7]}-{long_date[:4]}"
