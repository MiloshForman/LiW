def get_mask_card_number(card_number: int) -> str:
    """принимает на вход номер карты и возвращает его маску"""

    str_number = str(card_number)

    return f"{str_number[:4]} {str_number[4:6]}** **** {str_number[-4:]}"


def get_mask_account(account_number: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""

    str_account = str(account_number)

    return f"**{str_account[-4:]}"
