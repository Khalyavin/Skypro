class InvalidAgeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('__str__')
        if self.message:
            return self.message
        else:
            return 'InvalidAgeError has been raised'


def main():
    try:
        age = int(input('Введите ваш возраст: '))
        if age < 0 or age >= 120:
            raise InvalidAgeError('Извините, этот возраст не корректен')
        print(f'Вам {age} лет')
    except ValueError:
        print('Возраст должен быть числом')
    except InvalidAgeError as e:
        print(e)


if __name__ is main():
    main()