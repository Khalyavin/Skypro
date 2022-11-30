import csv
import os

path = '/home/vssl/PythonProject/lssn_24_30_11_22/'
data_file = 'all_stocks_5yr.csv'

data = []
dict_data = {}


# def get_by_data(date_='2017-08-08', name_='PCLN', filename_='dump.csv'):
def get_by_data(date='2017-08-08', name='PCLN', filename='dump.csv'):
    if (date, name) in dict_data.keys():
        header = ["date", "open", "high", "low", "close", "volume", "ticker"]
        full_file_path = path + filename

        if os.path.isfile(full_file_path):
            os.remove(full_file_path)

        with open(full_file_path, 'w', newline='') as csvfile:
            movies = csv.writer(csvfile)
            movies.writerow(header)
            lst = [date, dict_data[(date, name)][0], dict_data[(date, name)][1],
                   dict_data[(date, name)][2], dict_data[(date, name)][3],
                   dict_data[(date, name)][4], name]
            movies.writerow(lst)
            print(f'В файл {filename} записана строка {lst}')


def cach_data():
    """ создает словарь для поиска записи по полям 'date' и 'name'
    """
    for i in range(len(data)):
        dict_data.update({(data[i][0], data[i][6]): data[i][1:-1:]})


def unique_ticker_test(filename):
    """ Прооверяет тикер в filename на уникальность
    """
    full_path = path + filename
    tmp_data = []
    h = set()
    data.clear()

    with open(full_path, 'r') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            tmp_data.append(row)

    tmp_data = tmp_data[1::]

    for i in range(len(tmp_data)):
        if tmp_data[i][6] not in h:
            data.append(tmp_data[i])
            h.add(tmp_data[i][6])



def cutter(date, f_name):
    """ вырезает из больших данных данные одного дня и сбрасывает их в файл
    """
    full_path = path + data_file

    with open(full_path, 'r') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            if row[0] == date:
                data.append(row)


    header = ["date", "open", "high", "low", "close", "volume"]
    full_data_file = path + f_name

    if os.path.isfile(full_data_file):
        os.remove(full_data_file)

    with open(full_data_file, 'w', newline='') as csvfile:
        movies = csv.writer(csvfile)
        movies.writerow(header)
        for row in data:
            movies.writerow(row)


# cutter('2017-08-08', 'tmp_data.csv')
# В tmp_data лежит 503 записи с датой 2017-08-08

unique_ticker_test('tmp_data.csv')
# В data лежит готовые к хэшированию по  date и ticker данные

cach_data()
# готова хэш-таблица для полей 'date' и 'name'

get_by_data(date='2017-08-08', name='PCLN', filename='dump.csv')