import csv


class Item:
    pay_rate = 0.8  # Уровень оплаты после скидки 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Название слишком длинное!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        try:
            with open(file) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    all.append(row)
            print(all)
        except:
            print(f'FileNotFoundError: [Errno 2] No such file or directory: "{file}"')
        else:
            csvfile.close()

    def __str__(self):
        return f'{self.__class__}({self.__name}, {self.price}, {self.quantity})'


Item.instantiate_from_csv('items.csv')

for item in Item.all:
    print(item)