import pytest
from src.masks import get_mask_card_number, get_mask_account

#


def test_mask_card_number():
    assert (
        get_mask_card_number("Visa Platinum 7000792289606361")
        == "Visa Platinum 7000 79** **** 6361"
    )
    assert (
        get_mask_card_number("Maestro 1596837868705199")
        == "Maestro 1596 83** **** 5199"
    )


@pytest.fixture
def test_account():

    return "Счет **4305"


def test_with_fixture(test_account):
    assert test_account == get_mask_account("Счет 73654108430135874305")


def test_mask_account_number():
    assert get_mask_account("Счет 64686473678894779589") == "Счет **9589"
