#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, состоящую из двух списков Listbox. В первом будет,
например, перечень товаров, заданный программно. Второй изначально пуст, пусть это
будет перечень покупок. При клике на одну кнопку товар должен переходить из одного
списка в другой. При клике на вторую кнопку – возвращаться (человек передумал покупать).
Предусмотрите возможность множественного выбора элементов списка и их перемещения
"""

import sys
from PySide2.QtWidgets import QWidget, QApplication, QListWidget, QPushButton, QAbstractItemView, QVBoxLayout, \
    QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.list1 = QListWidget()
        self.list2 = QListWidget()
        self.list1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list1.addItems(shopping_list)
        self.butn1 = QPushButton("Добавить")
        self.butn2 = QPushButton("Удалить")
        self.butn1.clicked.connect(self.add)
        self.butn2.clicked.connect(self.delete)
        self.initialization()

    def initialization(self):
        self.setGeometry(200, 200, 400, 230)
        self.setWindowTitle("Задание 1")
        self.display_widgets()

    def display_widgets(self):
        h_box = QHBoxLayout()
        v_box = QVBoxLayout()
        h_box.addWidget(self.list1)
        h_box.addLayout(v_box)
        v_box.addWidget(self.butn1)
        v_box.addWidget(self.butn2)
        h_box.addWidget(self.list2)
        self.setLayout(h_box)

    def delete(self):
        general_list = self.list2.selectedItems()
        for i in general_list:
            self.list2.takeItem(self.list2.row(i))
            self.list1.addItem(i)

    def add(self):
        general_list = self.list1.selectedItems()
        for i in general_list:
            self.list1.takeItem(self.list1.row(i))
            self.list2.addItem(i)


if __name__ == "__main__":
    shopping_list = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple']
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
