class Employee:
    __slots__ = ('first', 'last')

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, value):
        self.first = value.split(' ')[0]
        self.last = value.split(' ')[1]

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'


emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = "Corey Schafer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)