class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

        self.__check(name, price, quantity)

    def __str__(self):
        self.__check(self.name, self.price, self.quantity)

        return (f'Item ({self.name}, {self.price}, {self.quantity})')

    def __check(self, name, price, quantity):
        if not isinstance(self.name, str):
            raise TypeError('Название товара должно быть строкой')

        if not isinstance(self.price, int) or isinstance(self.price, float):
            raise TypeError('Цена товара должна быть числом')

        if not isinstance(self.quantity, int):
            raise TypeError('Количество товара должно быть целым числом')


print(Item('phone', 18000, 5))

print(Item(18000, 'phone', 5))

print(Item('phone', '18000', 5))

print(Item('phone', 18000, 5.5))
