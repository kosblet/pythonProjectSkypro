import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_mask_card_number():
    """
    Тестирование функции маскировки номера карты. for push
    """
    assert (
        get_mask_card_number("Visa Platinum 7000 7922 8960 6361")
        == "Visa Platinum 7000 79** **** 6361"
    )
    assert (
        get_mask_card_number("Maestro 1596 8378 6870 5199")
        == "Maestro 1596 83** **** 5199"
    )
    assert get_mask_card_number("4111111111111111") == "4111 11** **** 1111"


@pytest.fixture
def test_account():
    """
    Фикстура для тестирования маскировки счета.
    """
    return "Счет **4305"


def test_with_fixture(test_account):
    """
    Тестирование функции маскировки счета с использованием фикстуры.
    """
    assert test_account == get_mask_account("Счет 73654108430135874305")


def test_mask_account_number():
    """
    Тестирование функции маскировки номера счета.
    """
    assert get_mask_account("Счет 64686473678894779589") == "Счет **9589"
    assert get_mask_account("Счет 1234567890123456") == "Счет **3456"
