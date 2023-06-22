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

class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, "main.ui")
        uic.loadUi(UI_File_Path, self)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = AdminWindow()
    window.show()
    app.exec()