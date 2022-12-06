class Todolist:
    """Класс списка задач"""

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Добавляет задачу в список"""
        self.tasks.append(task)


todo_list = Todolist()

todo_list.add_task('Купить лампочку')
todo_list.add_task('Поменять лампочку')
todo_list.add_task('Выкинуть лампочку')

print('\n'.join(todo_list.tasks))
