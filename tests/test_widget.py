import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "card_name, card_account_mask",
    [
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Visa 12345", "Неправильный номер"),
        (None, "Неправильный номер"),
    ],
)
def test_card_mask(card_name, card_account_mask):
    assert mask_account_card(card_name) == card_account_mask
