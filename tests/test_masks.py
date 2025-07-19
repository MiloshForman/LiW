from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.mark.parametrize(
    "card_number, card_mask",
    [(7000792289606361, "7000 79** **** 6361"), (123, "Неправильный номер карты"), (None, "Неправильный номер карты")],
)
def test_card_mask(card_number: int, card_mask: str):
    """Тестирует функцию get_mask_card_number

    на правильное маскирование номера карты, реакцию на некорректный входной номер
    и отсутствие входного номера

    """

    assert get_mask_card_number(card_number) == card_mask


@pytest.mark.parametrize(
    "account_number, account_mask",
    [(73654108430135874305, "**4305"), (123, "Неправильный номер карты"), (None, "Неправильный номер карты")],
)
def test_check_mask(account_number: int, account_mask: str):
    """Тестирует функцию get_mask_account

    на правильное маскирование номера счета, реакцию на некорректный входной номер
    и отсутствие входного номера

    """
    assert get_mask_account(account_number) == account_mask
