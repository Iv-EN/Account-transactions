from utils import get_data_from_file, sort_date_by_date, get_print_data

FILE_NAME = "data/operations.json"
"""Имя файла с данными об операциях."""
NUMBER_OPERATIONS_EXECUTED: int = 5
"""Количество выполненных (EXECUTED) операций для вывода на экран."""

def main() -> None:
    """Основная функция проекта."""
    no_sorted_data = get_data_from_file(FILE_NAME)
    sorted_data = sort_date_by_date(no_sorted_data, NUMBER_OPERATIONS_EXECUTED)
    for operation in sorted_data:
        print(get_print_data(operation))
if __name__ == "__main__":
    main()