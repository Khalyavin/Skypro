class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

        self.__check(name, price, quantity)

    def __str__(self):
        self.__check(self.name, self.price, self.quantity)

        return f'Item ({self.name}, {self.price}, {self.quantity}' + ')'

    def __check(self, name, price, quantity):
        if not isinstance(self.name, str):
            raise TypeError('Название товара должно быть строкой')

        if not isinstance(self.price, int) or isinstance(self.price, float):
            raise TypeError('Цена товара должна быть числом')

        if not isinstance(self.quantity, int):
            raise TypeError('Количество товара должно быть целым числом')


class Phone(Item):
    def __init__(self, name, price, quantity=0, broken=0):
        super().__init__(name, price, quantity)
        self.broken = broken

        self.__check(self.name, self.price, self.quantity, self.broken)

    def __str__(self):
        self.__check(self.name, self.price, self.quantity, self.broken)

        return f'Item ({self.name}, {self.price}, {self.quantity}, {self.broken})'

    def __check(self, name, price, quantity, broken):
        #        super().__check(name, price, quantity)
        if not isinstance(self.name, str):
            raise TypeError('Название товара должно быть строкой')

        if not isinstance(self.price, int) or isinstance(self.price, float):
            raise TypeError('Цена товара должна быть числом')

        if not isinstance(self.quantity, int):
            raise TypeError('Количество товара должно быть целым числом')

        if not isinstance(self.broken, int):
            raise TypeError('Количество бракованного товара должно быть целым числом')


phone1 = Phone("iPhone 10", 500, 5, 1)
print(phone1)
