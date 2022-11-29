import csv

full_path = '/home/vssl/PythonProject/kurs_SP500/all_stocks_5yr.csv'

def read_data(limit_, group_by_name_, ticker_):
    """ Наполняет массив данными из файла в зависимости от флага group_by_name"""
    data = []

    with open(full_path, 'r') as file:
        file_reader = csv.reader(file)
        cntr = 0
        for row in file_reader:
            if row[0] == 'date': continue
            if cntr < limit_ + 1:
                if not (group_by_name_ and ticker_):
                    data.append(row)
                else:
                    if row[6] == ticker_:
                        data.append(row)
                    else:
                        continue
                cntr += 1
                print(row)
            else:
                break
        print(data)

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

    read_data(limit, group_by_name, ticker)


select_sorted(limit=5, ticker='FLS', group_by_name=False)
