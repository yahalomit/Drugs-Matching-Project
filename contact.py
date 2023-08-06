# Yahalomit Levi 203956321
# Nisan Fichman 204470199

import os
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QPushButton,QComboBox,QMessageBox, QFileDialog
from PyQt6.QtCore import Qt,QRunnable, QThreadPool, QDate, QTime, QDateTime, QFileInfo
from PyQt6 import uic, QtGui

import DB.DataBase

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class contactWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, resource_path("GUIui/contact.ui"))
        uic.loadUi(UI_File_Path, self)
        self.show()

        self.firatNamelLineEdit.setMaxLength(15)
        self.lastNameLineEdit.setMaxLength(20)
        self.emailLineEdit.setMaxLength(25)
        self.phoneLineEdit.setMaxLength(10)


        self.submitBtn.clicked.connect(self.submitBtn_clicked)
            
    def submitBtn_clicked(self):
        if str(self.firatNamelLineEdit.text()) and str(self.lastNameLineEdit.text()) and str(self.emailLineEdit.text()) and\
                                            str(self.phoneLineEdit.text()) and str(self.textEdit.toPlainText()):
            if len(str(self.phoneLineEdit.text()))!=10:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("Phone number must be 10 digit")
                msgBox.setWindowTitle("Something went wrong")
                msgBox.exec()
            elif '@' not in str(self.emailLineEdit.text()) or '.' not in str(self.emailLineEdit.text()):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("Invalid Email address\n please inset email adress as follow:\n example@domain.com")
                msgBox.setWindowTitle("Something went wrong")
                msgBox.exec()
            else:
                if self.emailCheckBox.isChecked():
                    DB.DataBase.saveContactLettersToDB(str(self.firatNamelLineEdit.text()),str(self.lastNameLineEdit.text()),str(self.emailLineEdit.text()),
                                                        str(self.phoneLineEdit.text()),str(self.textEdit.toPlainText()), 'email')
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Icon.Information)
                    msgBox.setText("Message sent!")
                    msgBox.setWindowTitle("Greate Success")
                    msgBox.exec()
                    self.close()   
                elif self.phoneCheckBox.isChecked():
                    DB.DataBase.saveContactLettersToDB(str(self.firatNamelLineEdit.text()),str(self.lastNameLineEdit.text()),str(self.emailLineEdit.text()),
                                    str(self.phoneLineEdit.text()),str(self.textEdit.toPlainText()), 'phone')
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Icon.Information)
                    msgBox.setText("Message sent!")
                    msgBox.setWindowTitle("Greate Success")
                    msgBox.exec()
                    self.close()                       
                else:
                    DB.DataBase.saveContactLettersToDB(str(self.firatNamelLineEdit.text()),str(self.lastNameLineEdit.text()),str(self.emailLineEdit.text()),
                                str(self.phoneLineEdit.text()),str(self.textEdit.toPlainText()), 'none')
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Icon.Information)
                    msgBox.setText("Message sent!")
                    msgBox.setWindowTitle("Greate Success")
                    msgBox.exec()
                    self.close()        
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("Please fill in all the fields")
            msgBox.setWindowTitle("Something went wrong")
            msgBox.exec()


if __name__ == "__main__":
    app = QApplication([])
    window = contactWindow()
    window.show()
    app.exec()