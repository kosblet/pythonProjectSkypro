from typing import Union


#
def get_mask_card_number(num_card: Union[int, str]) -> str:
    card_name =
    num_card = str(num_card)
    block_1 = num_card[0:4]
    block_2 = num_card[5:7] + "**"
    block_3 = "****"
    block_4 = num_card[17:19]
    mask_card = block_1 + " " + block_2 + " " + block_3 + " " + block_4
    return mask_card


def get_mask_account(num_card: Union[int, str]) -> str:
    num_card = str(num_card)
    account_number_start = num_card.rfind(" ") + 1
    mask_account = num_card[:account_number_start] + "***" + num_card[-4:]
    return mask_account


print(get_mask_card_number("9999 5555 6666 3333"))
