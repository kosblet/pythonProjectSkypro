import pytest
from src.widget import get_date, mask_account_card
#for push

def test_convert_date():
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"


@pytest.fixture
def test_account():
    return "Счет **4305"


def test_with_fixture(test_account):
    assert test_account == mask_account_card("Счет 73654108430135874305")
