from PyQt6.QtWidgets import QMainWindow
from .ui import init_ui
from .tasks import load_todos, save_todos, add_todo, remove_todo

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Todo List')
        self.todo_file = './ToDoList/App/todos.json'
        self.init_ui()
        load_todos(self)

    def init_ui(self):
        init_ui(self)

    def save_todos(self):
        save_todos(self)

    def add_todo(self):
        add_todo(self)

    def remove_todo(self):
        remove_todo(self)
