class Team:
    """
    Хранит список джунов и синьоров, а также переопределяет метод __iter__().
    """

    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __iter__(self):
        """ Возвращает объект-итератор """
        return TeamIterator(self)

class TeamIterator:
    def __init__(self, team, start=0, stop=0, step=1):
        self._juniorMembers = team._juniorMembers
        self._seniorMembers = team._seniorMembers
        self.start = start
        self.stop = len(self._juniorMembers) + len(self._seniorMembers)
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self._juniorMembers[self.value] if self.value < len(self._juniorMembers) else self._seniorMembers[self.value - len(self._juniorMembers)]
        else:
            raise StopIteration


def main():
    # создаем команду
    team = Team()
    # добавляем имена джунов
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    # добавляем имена синьоров
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])

    print('*** Итерируемся по команде в цикле for ***')
    for member in team:
        print(member)

    print('*** Итерируемся по команде в цикле while ***')
    # Получаем итератор из итерируемого объекта - экземпляра класса Team
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    main()