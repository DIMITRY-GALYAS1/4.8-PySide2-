#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу по следующему описанию. Нажатие Enter в однострочном
текстовом поле приводит к перемещению текста из него в список. При
двойном клике по элементу-строке списка, она должна копироваться в
текстовое поле
"""

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, \
    QVBoxLayout, QListWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.list_write = QListWidget()
        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.move_txt)
        self.list_write.itemDoubleClicked.connect(self.copy_item)
        self.initialization()

    def initialization(self):
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle("Задание 2")
        self.display_widgets()

    def display_widgets(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.line_edit)
        v_box.addWidget(self.list_write)
        self.setLayout(v_box)

    def move_txt(self):
        self.list_write.addItem(self.line_edit.text())
        self.line_edit.clear()

    def copy_item(self):
        general_list = self.list_write.selectedItems()
        if not general_list:
            return
        for i in general_list:
            self.line_edit.setText(i.text())


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
