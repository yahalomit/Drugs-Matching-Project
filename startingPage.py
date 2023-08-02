# Yahalomit Levi 203956321
# Nisan Fichman 204470199

from datetime import datetime
import os
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QPushButton,QComboBox,QMessageBox, QFileDialog
from PyQt6.QtCore import Qt,QRunnable, QThreadPool, QDate, QTime, QDateTime, QFileInfo
from PyQt6 import uic, QtGui
from PyQt6.QtGui import QPixmap

import DB.DataBase

class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, "GUIui/main.ui")
        uic.loadUi(UI_File_Path, self)
        self.show()

        pixmap = QPixmap("media/warining-logo.jpg")
        self.label_4.setPixmap(pixmap)

        self.viewBtn1.clicked.connect(self.viewBtn1_clicked)
        self.viewBtn2.clicked.connect(self.viewBtn2_clicked)
        self.adminLoginBtn.clicked.connect(self.adminLoginBtn_clicked)
        self.contactUsBtn.clicked.connect(self.contactUsBtn_clicked)

        medNameList = DB.DataBase.getMedicationsNameList()
        for medication in medNameList:
            self.med1comboBox.addItem(medication)
            self.med2comboBox.addItem(medication)


    def viewBtn1_clicked(self):
        from generalInfo import generalInfoWindow
        self.window = generalInfoWindow(str(self.med1comboBox. currentText()))

    def viewBtn2_clicked(self):
        from generalInfo import generalInfoWindow
        self.window = generalInfoWindow(str(self.med2comboBox. currentText()))
    
    def adminLoginBtn_clicked(self):
        from login import LoginWindow
        self.window = LoginWindow()

    def contactUsBtn_clicked(self):
        from contact import contactWindow
        self.window = contactWindow()


if __name__ == "__main__":
    app = QApplication([])
    window = AdminWindow()
    window.show()
    app.exec()