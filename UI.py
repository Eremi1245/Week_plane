#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication,QLabel,)
from datetime import date



class Example(QWidget):

    def __init__(self,secondtable,firtstable,colors):
        super().__init__()
        # self.general_info=firtstable
        self.secondtable = secondtable
        self.firtstable=firtstable
        self.colors=colors


        self.initUI()

    def initUI(self):

        td=date.today()

        grid = QGridLayout()
        self.setLayout(grid)
        self.setGeometry(350,150,700,300)
        Monday=QLabel('Понедельник')
        Tuesday=QLabel('Вторник')
        Wednesday=QLabel('Среда')
        Thursday=QLabel('Четверг')
        Friday=QLabel('Пятница')
        Saturday=QLabel('Суббота')
        Sunday=QLabel('Воскресенье')
        positions = [(i, j) for i in range(1,8) for j in range(8)]
        for position, name in zip(positions, self.secondtable):
            button = QLabel(name)
            if len(name)==1:
                continue
            else:
                if td > date.fromisoformat(name[0:10]):\
                    button.setStyleSheet("background-color: grey")
                else:
                    button.setStyleSheet(f"background-color: {self.colors[name[13:]]}")
            grid.addWidget(button, *position)
        label=QLabel(self.firtstable)
        # label.setStyleSheet("background-color: blue");
        grid.addWidget(label, 0, 0, 7, 1)
        grid.addWidget(Monday, 0, 1)
        grid.addWidget(Tuesday, 0, 2)
        grid.addWidget(Wednesday, 0, 3)
        grid.addWidget(Thursday, 0, 4)
        grid.addWidget(Friday, 0, 5)
        grid.addWidget(Saturday, 0, 6)
        grid.addWidget(Sunday, 0, 7)
        self.setWindowTitle('Week Plane')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
