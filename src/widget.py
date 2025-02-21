from src import masks


def mask_account_card(card_info: str) -> str:
    index = 0
    for char in card_info:
        if char.isdigit():
            break
        index += 1

    prefix = card_info[
        :index
    ].strip()  # Убираем лишние пробелы в начале и конце префикса
    if prefix == "Счет":
        return f"{prefix} {masks.get_mask_account(card_info[index:].strip())}"
    else:
        return f"{prefix} {masks.get_mask_card_number(card_info[index:].strip())}"


def get_date(date: str) -> str:
    year, month, day = date[:10].split("-")
    return f"{day}.{month}.{year}"


# Примеры использования функций
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
