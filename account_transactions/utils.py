import datetime
import json
import re
from typing import Union


def get_data_from_file(file_name: str) -> list:
    """
    Получает данные из файла
    и возвращает их в виде списка.
    """
    with open(file_name, 'r') as f:
        content = f.read()
        data = json.loads(content)
    return data

def sort_date_by_date(no_sorted_data: list, number: int) -> list:
    """
    Сортирует полученные данные по дате
    и возвращает необходимое количество выполненных операций.
    """
    operations_for_withdrawal = []
    sorted_data = sorted(
        [item for item in no_sorted_data if item],
        key=lambda item:
        datetime.datetime.strptime(
        item["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=True
    )
    for operation in sorted_data:
        if len(operations_for_withdrawal) >= number:
            break
        if operation["state"] == "EXECUTED":
            operations_for_withdrawal.append(operation)
    return operations_for_withdrawal

def format_numbers(account_info: str) -> Union[str, None]:
    """Форматирует номер карты или счёта по указанным правилам."""
    groups = re.match(r"([а-яА-Яa-zA-Z\s]+)\s(\d+)", account_info, re.UNICODE)
    if groups:
        name, number = groups.groups()
        name = name.strip()
        if number.isdigit():
            if len(number) == 16:
                formatted = f"{number[:4]} {number[4: 6]}** **** {number[-4:]}"
            elif len(number) > 4:
                formatted = f"**{number[-4:]}"
            else:
                return "Неизвестный формат номера"
        else:
            return "Неверный формат"
        return f"{name} {formatted}"
    return None

def get_print_data(operation: dict):
    """Получает и форматирует информацию об операции."""
    date = datetime.datetime.strptime(operation["date"].split("T")[0],
                             "%Y-%m-%d").strftime("%d.%m.%Y")
    description = operation["description"]
    from_account = format_numbers(operation.get("from", "Нет данных"))
    to_account = format_numbers(operation.get("to", "Нет данных"))
    amount = operation["operationAmount"]["amount"]
    currency = operation["operationAmount"]["currency"]["name"]
    if from_account is not None:
        return (f"{date} {description}\n"
                f"{from_account} -> {to_account}\n"
                f"{amount} {currency}\n"
                "")
    return (f"{date} {description}\n"
            f"{to_account}\n"
            f"{amount} {currency}\n"
            "")
