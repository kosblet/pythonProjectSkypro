from typing import Union


def get_mask_card_number(num_card: Union[int, str]) -> str:
    """
    Маскирует номер карты, оставляя первые 4 цифры, следующие 2 цифры,
    затем звездочки вместо остальных, и последние 4 цифры.
    Если есть название карты (например, "Visa Platinum"), оно также сохраняется.
    """
    # Разделяем строку на название карты и номер
    parts = num_card.rsplit(" ", 4)  # Делим строку справа по последним 4 пробелам
    if len(parts) == 5:
        card_name = " ".join(
            parts[:-4]
        )  # Собираем название карты из всех частей до номера
        card_number = "".join(parts[-4:]).replace(" ", "")  # Номер карты без пробелов
    else:
        card_name = ""
        card_number = num_card.replace(
            " ", ""
        )  # Если нет названия, берем весь текст как номер

    # Маскируем номер карты
    block_1 = card_number[0:4]
    block_2 = (
        card_number[4:6] + "**"
    )  # Берем цифры с позиций 4 и 5 (без учета пробелов)
    block_3 = "****"
    block_4 = card_number[-4:]
    masked_number = f"{block_1} {block_2} {block_3} {block_4}"

    # Возвращаем результат с названием карты, если оно есть
    return f"{card_name} {masked_number}" if card_name else masked_number


def get_mask_account(num_card: Union[int, str]) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры и добавляя '**' перед ними.
    Например, "Счет 1234567890123456" станет "Счет **3456".
    """
    num_card = str(num_card)
    account_number_start = num_card.rfind(" ") + 1
    account_number = num_card[account_number_start:]
    masked_account = f"**{account_number[-4:]}"
    return f"{num_card[:account_number_start]}{masked_account}"
