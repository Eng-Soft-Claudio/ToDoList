from PyQt6.QtWidgets import QApplication
from App.app import TodoApp

if __name__ == '__main__':
    app = QApplication([])
    window = TodoApp()
    window.show()
    app.exec()
