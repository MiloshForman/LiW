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
def test_card_mask(card_name: str, card_account_mask: str):
    """Тестирует функцию mask_account_card

    на корректное распознавание и применение нужного типа маскировки
    в зависимости от типа входных данных (карта или счет),
    на обработку некорректных входных данных и проверяет ее устойчивость к ошибкам.

    """

    assert mask_account_card(card_name) == card_account_mask


@pytest.mark.parametrize(
    "long_date, short_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("T02:26:18.671407D2024-03-11", "Неверный формат"),
        (None, "Неверный формат"),
    ],
)
def test_get_date(long_date: str, short_date: str):
    """Тестирует функцию get_date

    на правильность преобразования даты, реакцию на некорректный формат
    и на входные строки, где дата отсутствует

    """
    assert get_date(long_date) == short_date
