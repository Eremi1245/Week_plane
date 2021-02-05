from PyQt5 import QtWidgets
from Ui2 import *  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self,secondtable,firtstable,colors):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,secondtable,firtstable,colors)


app = QtWidgets.QApplication([])
application = mywindow('gfdgfd')
application.show()
sys.exit(app.exec())