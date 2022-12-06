class DataBase:
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")

    single_connect = None
    def __new__(DataBase, *args, **kwargs):
        if DataBase.single_connect is None:
            DataBase.single_connect = super().__new__(DataBase)
        return DataBase.single_connect


a = DataBase('123', '456', '789')
b = DataBase('987', '444', '321')
print(a is b)