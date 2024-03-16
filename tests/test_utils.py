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
    )
    assert executed, (
        "Полученные данные должны содержать "
        "только исполненные операции (state: EXECUTED)"
    )

def test_format_numbers():
    card_number = "Maestro 1596837868705199"
    account_number = "Счет 64686473678894779589"
    format_card = utils.format_numbers(card_number)
    format_account = utils.format_numbers(account_number)
    assert format_card == "Maestro 1596 83** **** 5199", (
       "номер карты должен выводиться в формате <Name XXXX XX** **** XXXX>"
    )
    assert format_account == "Счет **9589", (
        "номер счёта должен выводиться в формате <Счет **XXXX>"
    )

def test_get_print_data():
    operation = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    output_lines = utils.get_print_data(operation)
    assert output_lines == ("26.08.2019 Перевод организации\n"
                            "Maestro 1596 83** **** 5199 -> Счет **9589\n"
                            "31957.58 руб.\n"
                            "")