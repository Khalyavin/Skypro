class MyList(list):
    def __init__(self, values=None):
        super().__init__()
        if values is None:
            self.value = []
        else:
            self.value = values
        print('Работает магический метод 1')

    def __getitem__(self, key):
        print('Работает магический метод 2')
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value
        print('Работает магический метод 3')

    def __str__(self):
        print('Работает магический метод 4')
        return str(self.value)

    def __len__(self):
        print('Работает магический метод 5')
        return len(self.value)


lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'


print(lst)
print(len(lst))