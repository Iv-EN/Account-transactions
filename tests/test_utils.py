from account_transactions import utils

file = "account_transactions/data/operations.json"

def test_get_data_from_file():
    assert type(utils.get_data_from_file(file)) == list, (
        "Полученные данные должны быть списком."
    )

def test_sort_date_by_date():
    no_sort = utils.get_data_from_file(file)
    sort_data = utils.sort_date_by_date(no_sort, 5)
    executed = True
    for data in sort_data:
        if data["state"] != "EXECUTED":
            executed = False
    assert len(sort_data) == 5, (
        "Полученные данные должны быть списком из 5 элементов"
        "и содержать только исполненные операции (state: EXECUTED)"
    )
    assert executed, (
        "Полученные данные должны содержать "
        "только исполненные операции (state: EXECUTED)"
    )

def test_format_numbers():
    card_number = "Maestro 1596837868705199"
    account_number = "64686473678894779589"
    format_card = utils.format_numbers(card_number)
    format_account = utils.format_numbers(account_number)
    assert format_card == "1596 83** **** 5199", (
       "номер карты должен выводиться в формате XXXX XX** **** XXXX"
    )
    assert format_account == "**9589", (
        "номер счёта должен выводиться в формате **XXXX"
    )