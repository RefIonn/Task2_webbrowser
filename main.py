import os
import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QInputDialog, QLineEdit
from PyQt5.QtWidgets import QApplication, QMainWindow
import webbrowser


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__() #Создание окна

        self.setWindowTitle('Запрос в интернет') #Наименование окна
        self.setGeometry(700, 250, 500, 200)

        self.text2 = QtWidgets.QLabel(self)
        self.text2.setText('Поиск в интернете')
        self.text2.move(200, 20)
        self.text2.adjustSize()

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(150, 100, 230, 26)
        self.comboBox.setObjectName('ComboBox')
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "Yandex")
        self.comboBox.setItemText(1, "Google")
        self.value = self.comboBox.currentText()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Начать поиск")
        self.btn.move(200, 130)
        self.btn.clicked.connect(self.link)
        self.btn.adjustSize()

        self.edit = QtWidgets.QPlainTextEdit(self)
        self.edit.setPlaceholderText("Поисковая фраза")
        self.edit.setGeometry(50, 50, 400, 46)

    def link(self):
        text = self.edit.toPlainText()
        if self.value == "Yandex":
            webbrowser.open(f"https://ya.ru/search/?text={text}")
        else:
            webbrowser.open(f"https://www.google.com/search?q={text}")


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
