# Yahalomit Levi 203956321
# Nisan Fichman 204470199

from datetime import datetime
import os
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QPushButton,QComboBox,QMessageBox, QFileDialog
from PyQt6.QtCore import Qt,QRunnable, QThreadPool, QDate, QTime, QDateTime, QFileInfo
from PyQt6 import uic, QtGui

import DB.DataBase

class createAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, "GUIui/createAdmin.ui")
        uic.loadUi(UI_File_Path, self)
        self.show()

        self.nameLineEdit.setMaxLength(15)
        self.lastNameLineEdit.setMaxLength(20)
        self.idLineEdit.setMaxLength(9)
        self.licenseLineEdit.setMaxLength(5)
        self.passwordLineEdit.setMaxLength(12)
        self.confPassordLineEdit.setMaxLength(12)


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
            else:
                DB.DataBase.createNewAdmin(str(self.nameLineEdit.text()), str(self.lastNameLineEdit.text()), str(self.idLineEdit.text())
                                    ,str(self.emailLineEdit.text()), str(self.licenseLineEdit.text()), str(self.passwordLineEdit.text()))
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