# Yahalomit Levi 203956321
# Nisan Fichman 204470199

from datetime import datetime
import os
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QPushButton,QComboBox,QMessageBox, QFileDialog
from PyQt6.QtCore import Qt,QRunnable, QThreadPool, QDate, QTime, QDateTime, QFileInfo
from PyQt6 import uic, QtGui

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, resource_path("addMedication.ui"))
        uic.loadUi(UI_File_Path, self)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = AdminWindow()
    window.show()
    app.exec()