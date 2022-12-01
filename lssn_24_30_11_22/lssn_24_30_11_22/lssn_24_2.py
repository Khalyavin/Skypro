import csv
import os
from functools import wraps
from kurs_SP500.kurs_SP500.kurs_SP500 import read_data, sort_data, write_data

path = '/home/vssl/PythonProject/kurs_SP500/'
data_file = 'all_stocks_5yr.csv'
full_path = path + data_file
# source_file = 'kurs_sp500/kurs_SP500.py'
# source_path = path + source_file

data = []
def cached(func):
    """ Декоратор кеширования функции. За ключ принимаю аргументы функции без файла вывода.
    Если вызов с указанными аргументами уже совершался, то значение беру из словаря.
    Если такой набор аргументов встречается впервые, считаю функцию, заношу ее в словарь.
    """
    cach_dict = {}
    @wraps()
    def inner(sort_columns=None, limit=20, order='asc', group_by_name=True, ticker=None, filename=dump.csv ):
        if (sort_columns, limit, order, group_by_name, ticker) in cach_dict.keys():
            return cach_dict[(sort_columns, limit, order, group_by_name, ticker)]
        else:
            cach_dict.update({(sort_columns, limit, order, group_by_name, ticker):
                                  func(sort_columns_=sort_columns, limit_=limit, order_=order,
                                       group_by_name_=group_by_name, ticker_=ticker, filename_=filename)})
            return cach_dict[(sort_columns, limit, order, group_by_name, ticker)]
    return inner

    write_data(filename)

@cached
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
