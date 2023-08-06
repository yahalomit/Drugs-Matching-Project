# Yahalomit Levi 203956321
# Nisan Fichman 204470199

from datetime import datetime
import os
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QPushButton,QComboBox,QMessageBox, QFileDialog, QLineEdit
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

class createAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, resource_path("GUIui/createAdmin.ui"))
        uic.loadUi(UI_File_Path, self)
        self.show()

        self.nameLineEdit.setMaxLength(15)
        self.lastNameLineEdit.setMaxLength(20)
        self.idLineEdit.setMaxLength(9)
        self.licenseLineEdit.setMaxLength(5)
        self.passwordLineEdit.setMaxLength(12)
        self.confPassordLineEdit.setMaxLength(12)


        pixmap = QPixmap(resource_path("media/pharmacist-logo.jpg"))
        self.label_6.setPixmap(pixmap)

        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confPassordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.createAdminBtn.clicked.connect(self.clicked_createAdminBtn)

    def clicked_createAdminBtn(self):
        if (self.nameLineEdit.text() and self.lastNameLineEdit.text() and self.idLineEdit.text() and self.emailLineEdit.text() and self.licenseLineEdit.text()
            and self.passwordLineEdit.text() and  self.confPassordLineEdit.text()):
            if len(str((self.idLineEdit.text()))) != 9:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("ID number must be 9 digit")
                msgBox.setWindowTitle("Something went wrong")
                msgBox.exec()
            elif len(str((self.licenseLineEdit.text()))) != 5:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("Licence number must be 5 digit")
                msgBox.setWindowTitle("Something went wrong")
                msgBox.exec()
            elif len(str((self.licenseLineEdit.text()))) != 5:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("Licence number must be 5 digit")
                msgBox.setWindowTitle("Something went wrong")
                msgBox.exec()
            elif len(str(self.passwordLineEdit.text())) < 6:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("password must be at least 6 digit")
                msgBox.setWindowTitle("Something went wrong")
                msgBox.exec()
            elif self.passwordLineEdit.text()!=self.confPassordLineEdit.text():
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("Passord and confirmantion are not identical")
                msgBox.setWindowTitle("Something went wrong")
                msgBox.exec()
            elif DB.DataBase.checkAdminData(str(self.idLineEdit.text()), str(self.licenseLineEdit.text())) != True:
                result = DB.DataBase.checkAdminData(str(self.idLineEdit.text()), str(self.licenseLineEdit.text()))
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText(result + " is already exist")
                msgBox.setWindowTitle("Something went wrong")
                msgBox.exec()
            else:
                result = DB.DataBase.createNewAdmin(str(self.nameLineEdit.text()), str(self.lastNameLineEdit.text()), str(self.idLineEdit.text())
                                                    , str(self.emailLineEdit.text()), str(self.licenseLineEdit.text()), str(self.passwordLineEdit.text()))
                if result != None:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Icon.Critical)
                    msgBox.setText(result)
                    msgBox.setWindowTitle("Something went wrong")
                    msgBox.exec()
                else:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Icon.Critical)
                    msgBox.setText("New admin is created")
                    msgBox.setWindowTitle("Succeed")
                    msgBox.exec()
                    self.close()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("One or more of the details you insert are invalid")
            msgBox.setWindowTitle("Something went wrong")
            msgBox.exec()


if __name__ == "__main__":
    app = QApplication([])
    window = createAdminWindow()
    window.show()
    app.exec()