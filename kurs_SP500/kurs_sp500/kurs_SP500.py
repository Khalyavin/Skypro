import csv
import os

path = '/home/vssl/PythonProject/kurs_SP500/'
data_file = 'all_stocks_5yr.csv'
full_path = path + data_file

data = []


def read_data(limit_, group_by_name_, ticker_):
    """ Наполняет массив данными из файла в зависимости от флага group_by_name"""

    with open(full_path, 'r') as file:
        file_reader = csv.reader(file)
        cntr = 0
        for row in file_reader:
            if row[0] == 'date': continue
            if cntr < limit_:
                if not (group_by_name_ and ticker_):
                    data.append(row)
                else:
                    if row[6] == ticker_:
                        data.append(row)
                    else:
                        continue
                cntr += 1
            else:
                break


def sort_data(sort_columns_, order_):
    """ сортирует список data по полю
     sort_columns: ["date", "open", "high", "low", "close", "volume"]
    в порядке order: ["asc", "desc"]
    """
    # Разбираюсь что сортироавать
    sort_col = ["date", "open", "high", "low", "close", "volume"]
    if sort_columns_ == "date": col = 0
    elif sort_columns_ == "open": col = 1
    elif sort_columns_ == "high": col = 2
    elif sort_columns_ == "low": col = 3
    elif sort_columns_ == "close": col = 4
    elif sort_columns_ == "volume":  # Остальные поля сортируются типом str, а это - переменной длинны
        col = 5
        for i in range(len(data)):
            data[i][col] = int(data[i][col])
    else:
        return

    # Так как массив "небольшой", реализую классику - bubble sort
    cur_element = len(data)
    while cur_element > 1:
        for i in range(1, cur_element):
            if data[i - 1][col] > data[i][col]:
                data[i - 1], data[i] = data[i], data[i - 1]
            else:
                continue
        cur_element -= 1
    for i in range(len(data)):
        data[i][col] = str(data[i][col])
        # Теперь в data все элементы - string, готовы к dump to file

    if order_ == 'desc':  # Переворачиваю массив data
        for i in range(len(data) // 2):
            data[i], data[len(data) - i - 1] = data[len(data) - i - 1], data[i]


def write_data(f_name):
    """ Сбрасывает подготовенный список data в файл
    """
    header = ["date", "open", "high", "low", "close", "volume"]
    full_data_file = path + f_name

    if not f_name:  # В запросе нет файла, вывожу на экран
        for i in range(len(data)):
            print(data[i])
    else:
        if os.path.isfile(full_data_file):
            os.remove(full_data_file)

        with open(full_data_file, 'w', newline='') as csvfile:
            movies = csv.writer(csvfile)
            movies.writerow(header)
            for row in data:
                movies.writerow(row)


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
    # в списке data лежит limit строк по условию group_by_name

    sort_data(sort_columns, order)
    # в списке data лежат отсортированные limit строк по условию order

    write_data(filename)
    # отсортированные данные сброшены в файл filename


select_sorted(sort_columns="volume", order="asc", limit=5, ticker='FLS', group_by_name=True)
