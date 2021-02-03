#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication,QLabel)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['1', '2', '3', '4', '5', '6', '7',
                 '1', '2', '3', '4', '5', '6', '7',
                 '1', '2', '3', '4', '5', '6','7',
                 '1', '2', '3', '4', '5', '6', '7',
                 '1', '2', '3', '4', '5', '6', '7',
                 '1', '2', '3', '4', '5','6', '7',
                 '1', '2', '3', '4', '5', '6', '7']

        positions = [(i, j) for i in range(1,7) for j in range(1,8)]

        label=QLabel(f'Интересы\n'
                     f'цели\n'
                     f'месяц\n'
                     f'бабушка\n')
        grid.addWidget(label, 0, 0, 6, 1)
        for position, name in zip(positions, names):
            button = QPushButton(name)
            grid.addWidget(button, *position)
        self.move(300, 150)
        self.setWindowTitle('Week Plane')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
