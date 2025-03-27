from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget

def init_ui(self):
    central_widget = QWidget()
    self.setCentralWidget(central_widget)
    layout = QVBoxLayout()
    central_widget.setLayout(layout)

    self.input_field = QLineEdit()
    self.input_field.setPlaceholderText('Adicione uma nova tarefa...')
    layout.addWidget(self.input_field)

    add_button = QPushButton('Adicionar')
    add_button.clicked.connect(self.add_todo)
    layout.addWidget(add_button)

    self.todo_list = QListWidget()
    layout.addWidget(self.todo_list)

    remove_button = QPushButton('Remover Selecionada')
    remove_button.clicked.connect(self.remove_todo)
    layout.addWidget(remove_button)
