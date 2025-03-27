import json
from datetime import datetime

def load_todos(self):
    try:
        with open(self.todo_file, 'r') as file:
            todos = json.load(file)
            self.todo_list.addItems(todos)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

def save_todos(self):
    todos = [self.todo_list.item(i).text() for i in range(self.todo_list.count())]
    with open(self.todo_file, 'w') as file:
        json.dump(todos, file)

def add_todo(self):
    task = self.input_field.text().strip()
    if task:
        date = datetime.now().strftime('%d/%m/%Y')
        self.todo_list.addItem(f"{task} (Adicionado em: {date})")
        self.input_field.clear()
        save_todos(self)

def remove_todo(self):
    for item in self.todo_list.selectedItems():
        self.todo_list.takeItem(self.todo_list.row(item))
    save_todos(self)
