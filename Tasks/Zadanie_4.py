#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Создать изображение на холсте
"""

import sys
import random
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPainter, QBrush, QPen, QPolygon, QColor
from PySide2.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задание 4")
        self.setGeometry(300, 300, 600, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.darkRed, 3, Qt.SolidLine))  # Цвет и линия обводки
        painter.setBrush(QColor(255, 0, 0, 127))
        painter.drawRect(215, 200, 253, 281)  # корпус домика
        painter.setPen(QPen(Qt.darkRed, 3, Qt.SolidLine))
        painter.setBrush((QBrush(Qt.white)))
        painter.drawRect(305, 300, 70, 70)  # окно
        painter.drawLine(305, 335, 373, 335)  # Рама окна по горизонтали
        painter.drawLine(340, 300, 340, 367)  # Рама окна по вертикали
        painter.setBrush((QBrush(Qt.black)))
        points = QPolygon([
            QPoint(215, 200),
            QPoint(338, 70),
            QPoint(469, 200)  # Крыша
        ])
        painter.drawPolygon(points)
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
        painter.drawEllipse(490, 6, 80, 80)  # Солнце
        self.draw_grass(painter)
        self.draw_mouse(painter)

    def draw_grass(self, painter):
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.darkGreen, 2, Qt.SolidLine))
        painter.setBrush(Qt.darkGreen)
        for i in range(63):
            painter.drawArc(random.randint(1, 5), 417, i * 15, 360, 0 * 100, random.randint(50, 55) * 11)

    def draw_mouse(self, painter):
        painter.begin(self)
        points2 = QPolygon([
            QPoint(104, 458),
            QPoint(82, 450),
            QPoint(88, 473),
            QPoint(79, 473),
            QPoint(79, 487),
            QPoint(92, 486)
        ])
        points3 = QPolygon([
            QPoint(144, 457),
            QPoint(168, 452),
            QPoint(161, 473),
            QPoint(170, 473),
            QPoint(170, 487),
            QPoint(158, 487)
        ])
        points5 = QPolygon([
            QPoint(141, 449),
            QPoint(149, 446),
            QPoint(159, 438),
            QPoint(169, 429),
            QPoint(175, 423),
            QPoint(171, 432),
            QPoint(162, 442),
            QPoint(151, 451),
            QPoint(143, 456)
        ])
        points4 = QPolygon([
            QPoint(124, 411),
            QPoint(92, 486),
            QPoint(158, 487)
        ])
        painter.setPen(QPen(Qt.gray))
        painter.setBrush(QBrush(Qt.darkGray))
        painter.drawEllipse(78, 351, 40, 40)
        painter.drawEllipse(132, 359, 40, 40)
        points1 = QPolygon([
            QPoint(71, 423),
            QPoint(126, 364),
            QPoint(158, 423)
        ])
        painter.drawPolygon(points3)
        painter.drawPolygon(points2)
        painter.drawPolygon(points5)
        painter.drawPolygon(points4)
        painter.drawPolygon(points1)
        painter.drawRect(101, 482, 19, 12)
        painter.drawRect(130, 482, 19, 12)
        painter.setPen(QPen(Qt.black))
        painter.drawLine(83, 481, 83, 486)
        painter.drawLine(87, 481, 87, 486)
        painter.drawLine(139, 488, 139, 493)
        painter.drawLine(143, 488, 143, 493)
        painter.drawLine(109, 488, 109, 493)
        painter.drawLine(106, 488, 106, 493)
        painter.drawLine(166, 481, 166, 486)
        painter.drawLine(162, 481, 162, 486)
        painter.setPen(QPen(Qt.red))
        painter.setBrush(QBrush(Qt.darkRed))
        painter.drawEllipse(66, 415, 13, 13)
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(92, 382, 20, 20)
        painter.drawEllipse(114, 388, 20, 20)
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(100, 390, 5, 5)
        painter.drawEllipse(120, 395, 5, 5)
        painter.drawLine(65, 422, 47, 412)
        painter.drawLine(64, 423, 45, 419)
        painter.drawLine(65, 424, 46, 426)
        painter.drawLine(79, 422, 96, 412)
        painter.drawLine(80, 423, 100, 419)
        painter.drawLine(79, 424, 99, 426)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
