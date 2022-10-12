#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Изучите приведенную программу и самостоятельно запрограммируйте
постепенное движение фигуры в ту точку холста, где пользователь
кликает левой кнопкой мыши. Координаты события хранятся в его
атрибутах x и y (event.x , event.y)
"""

import sys
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import QPropertyAnimation, QPoint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задание 5")
        self.resize(500, 500)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color: green;border-radius: 25%;")
        self.child.resize(50, 50)
        self.animation = QPropertyAnimation(self.child, b"pos")
        self.animation.setDuration(1500)

    def mousePressEvent(self, event):
        self.animation.setEndValue(QPoint(event.x() - 25, event.y() - 25))
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
