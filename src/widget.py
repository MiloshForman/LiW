from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime
import re


def mask_account_card(card_name: str = "0") -> str:
    """Принимает тип-номер карты или счета card_name и возвращает замаскированный номер card_mask"""

    card_word = ""
    card_number = ""
    card_mask = ""

    if card_name == None:
        card_name = "0"

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
        return "Неправильный номер"

    return card_mask


def get_date(long_date: str = "0") -> str:
    """принимает на вход строку с датой long_date и отдает корректный результат в формате 'ДД.ММ.ГГГГ'"""

    if long_date == None:
        long_date = "0"

    if re.fullmatch(r"\d{4}-\d{2}-\d{2}\w\d{2}:\d{2}:\d{2}\.\d{6}", long_date):
        parsed_date = datetime.strptime(long_date, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = parsed_date.strftime("%d.%m.%Y")

        return formatted_date

    else:
        return "Неверный формат"
