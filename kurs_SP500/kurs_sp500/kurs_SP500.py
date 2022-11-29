import csv

def select_sorted(sort_columns=None, limit=20, order='asc', group_by_name=True,
                  ticker=None, filename='dump.csv'):
    """ Функция выбора и сортировки данных по S&P_500. Параметры:
    sort_columns: // одно из значений ["date", "open", "high", "low", "close", "volume"]
    limit: // количество выводимых строк, по умолчанию - 20
    order: // одно из значений ["asc", "desc"] - по умолчанию сортирует по возрастанию sort_columns
    group_by_name: // группировка по тикеру компании
    ticker: // тикер компании для выборки
    fliename: // файл для сохранения полученной выборки
    """

    with open('/home/vssl/PythonProject/kurs_SP500/all_stocks_5yr.csv', 'r') as file:
        file_reader = csv.reader(file)
        cntr = 0
        for row in file_reader:
             if cntr < limit + 1:
                cntr += 1
                print(row)
             else:
                 break

select_sorted(limit=5)