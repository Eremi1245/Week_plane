# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delinterestUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from core import connect,query_with_fetchall

class Ui_DelInterest(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(299, 487)
        _translate = QtCore.QCoreApplication.translate
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 380, 281, 61))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 281, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('')
        self.comboBox.setItemText(0, _translate("MainWindow", ""))
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 50, 281, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem('')
        self.comboBox_2.setItemText(0, _translate("MainWindow", ""))
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 90, 281, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem('')
        self.comboBox_3.setItemText(0, _translate("MainWindow", ""))
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 130, 281, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem('')
        self.comboBox_4.setItemText(0, _translate("MainWindow", ""))
        query=query_with_fetchall('inter_goal')
        interests={x[0] for x in query}
        count=1
        for i in interests:
            self.comboBox.addItem('')
            self.comboBox.setItemText(count, _translate("MainWindow", i))
            self.comboBox_2.addItem('')
            self.comboBox_2.setItemText(count, _translate("MainWindow", i))
            self.comboBox_3.addItem('')
            self.comboBox_3.setItemText(count, _translate("MainWindow", i))
            self.comboBox_4.addItem('')
            self.comboBox_4.setItemText(count, _translate("MainWindow", i))
            count+=1
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Удалить"))
