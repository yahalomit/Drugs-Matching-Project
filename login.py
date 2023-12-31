# Yahalomit Levi 203956321
# Nisan Fichman 204470199

import os
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QComboBox, QMessageBox, \
    QFileDialog, QLineEdit
from PyQt6.QtCore import Qt,QRunnable, QThreadPool, QDate, QTime, QDateTime, QFileInfo
from PyQt6 import uic, QtGui
from PyQt6.QtGui import QPixmap
import DB.DataBase

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, resource_path("GUIui/login.ui"))
        uic.loadUi(UI_File_Path, self)
        self.show()

        pixmap = QPixmap(resource_path("media/pharmeci-logo.png"))
        self.label_3.setPixmap(pixmap)

        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.submitBtn.clicked.connect(self.submitBtn_clicked)
    def submitBtn_clicked(self):
        if len(str(self.emailLineEdit.text())) != 0 and len(str(self.passwordLineEdit.text())) != 0:
            AdminFullName = DB.DataBase.signin(str(self.emailLineEdit.text()), str(self.passwordLineEdit.text()))
            print(AdminFullName)
            if AdminFullName!= None:
                from admin import AdminWindow
                self.window = AdminWindow(AdminFullName)
                self.close()
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("Some of the details you insert are inccorct\n please try again")
                msgBox.setWindowTitle("Something went wrong")
                msgBox.exec()

if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec()