def get_mask_card_number(card_number: int = 0) -> str:
    """принимает на вход номер карты card_number и возвращает его маску"""

    str_number = str(card_number)

    if len(str_number) == 16:
        return f"{str_number[:4]} {str_number[4:6]}** **** {str_number[-4:]}"
    else:
        return "Неправильный номер карты"


def get_mask_account(account_number: int = 0) -> str:
    """принимает на вход номер счета account_number и возвращает его маску"""

    str_account = str(account_number)

    if len(str_account) == 20:
        return f"**{str_account[-4:]}"
    else:
        return "Неправильный номер карты"
