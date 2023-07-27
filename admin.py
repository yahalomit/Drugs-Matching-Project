# Yahalomit Levi 203956321
# Nisan Fichman 204470199

from datetime import datetime
import os
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QPushButton,QComboBox,QMessageBox, QFileDialog
from PyQt6.QtCore import Qt,QRunnable, QThreadPool, QDate, QTime, QDateTime, QFileInfo
from PyQt6 import uic, QtGui

class AdminWindow(QMainWindow):
    def __init__(self, adminFullName):
        super().__init__()
        AdminFullName = adminFullName
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, "GUIui/admin.ui")
        uic.loadUi(UI_File_Path, self)
        self.show()

        self.helloLable.setText("Hello " + AdminFullName)

        self.logoutBtn.clicked.connect(self.clicked_logout)

        self.actionCreate_new_Admin.triggered.connect(self.action_Create_new_Admin)


    def clicked_logout(self):
        from login import LoginWindow
        self.window = LoginWindow()
        self.close()

    def action_Create_new_Admin(self):
        from createAdmin import createAdminWindow
        self.window = createAdminWindow()

if __name__ == "__main__":
    app = QApplication([])
    window = AdminWindow()
    window.show()
    app.exec()