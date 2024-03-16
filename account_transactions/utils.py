import json
import datetime
import re

FILE_NAME = "account_transactions/data/operations.json"
"""Имя файла с данными об операциях."""
NUMBER_OPERATIONS_EXECUTED = 5
"""Количество выполненных (EXECUTED) операций для вывода на экран."""

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
    и возвращает необходимое количество выполненных операций."""
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

def format_numbers(account_info: str) -> str:
    """Форматирует номер карты или счёта по указанным правилам."""
    numbers = re.findall(r'\d+', account_info)
    if numbers:
        num = numbers[0]
        if len(num) == 16:
            formatted = f"{num[:4]} {num[4: 6]}** **** {num[-4:]}"
            return formatted
        else:
            formatted = f"**{num[-4:]}"
            return formatted
    return "Не удалось получить номер карты или счёта"



def get_print_data(operation: list) -> tuple:
    """
    Получает необходимые для вывода данные
    и приводит их необходимому виду.
    """


file = FILE_NAME
no_sort = get_data_from_file(file)
sort_data = sort_date_by_date(no_sort, NUMBER_OPERATIONS_EXECUTED)
print(sort_data)
print(len(sort_data))