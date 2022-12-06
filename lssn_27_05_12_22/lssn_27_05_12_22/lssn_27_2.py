class Bottle:
    """Создал класс бутылок - цвет и наполненность"""
    def __init__(self, color, contains=0):
        self.color = color
        self.contains = contains

    def get_content(self):
        """Возвращает наполненность бутылки"""
        return self.contains

    def fill(self, volume):
        """'Доливает' в бутылку указанное количество жидкости"""
        self.contains += volume
        return self.contains



bottle_1 = Bottle('Красная')
bottle_2 = Bottle('Белая')

print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())

print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(-100)
print(bottle_2.color, bottle_2.get_content())
