# Account-transactions

## Описание

Это виджет, который показывает несколько последних успешных банковских операций клиента.

Выводит на экран список из 5 последних выполненных клиентом операций в формате:

<дата перевода> <описание перевода>  
<откуда> -> <куда>  
<сумма перевода> <валюта>  

(Данные берутся из файла ```data/operations.json```)

### Пример вывода для одной операции:
```commandline
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
```
## Запуск проекта
1. Клонировать репозиторий:
    ```bash
    git clone https://github.com/Iv-EN/Account-transactions.git
    ```

2. Создать и активировать виртуальное окружение:  
    Для Linux:
    ```bash
    python3 -m venv venv
    ```
   ```bash
   source venv/bin/activate
   ```
    Для Windows:
   ```bash
   python -m venv venv
   ```
   ```bash
   venv\Scripts\activate.bat
   ```

3. Обновить pip и установить зависимости из ```requirements.txt```
   ```bash
   python -m pip install --upgrade pip
   ```
   ```bash
   pip install -r requirements.txt
    ```
4. Запустить проект:
    ```bash
    python main.py
    ```

**Автор проекта:** [Evgeniy_Ivanov](https://github.com/Iv-EN/)

