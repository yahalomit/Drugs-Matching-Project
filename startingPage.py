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

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap


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
        UI_File_Path = os.path.join(script_path, resource_path("GUIui/main.ui"))
        uic.loadUi(UI_File_Path, self)
        self.show()

        pixmap = QPixmap(resource_path("media/warining-logo.jpg"))
        self.label_4.setPixmap(pixmap)

        self.viewBtn1.clicked.connect(self.viewBtn1_clicked)
        self.viewBtn2.clicked.connect(self.viewBtn2_clicked)
        self.adminLoginBtn.clicked.connect(self.adminLoginBtn_clicked)
        self.contactUsBtn.clicked.connect(self.contactUsBtn_clicked)
        self.metchBtn.clicked.connect(self.metchBtn_clicked)
        self.mainExportBtn.clicked.connect(self.mainExportBtn_clicked)


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

    def metchBtn_clicked(self):
        result = DB.DataBase.metchMedications(str(self.med1comboBox. currentText()),str(self.med2comboBox. currentText()))
        if result:
            self.textBrowser.clear()
            self.textBrowser.setText(result)
        else:
            self.textBrowser.setText("no contradiction was found")

    def mainExportBtn_clicked(self):
        title = str(self.med1comboBox. currentText())+" vs "+str(self.med2comboBox. currentText())
        content = str(self.textBrowser.toPlainText())
        filename, _ = QFileDialog.getSaveFileName(self, "Export PDF", "", "PDF files (*.pdf)")
        if filename:
            try:
                # Create a new PDF canvas
                c = canvas.Canvas(filename, pagesize=letter)

                # Set the title font and size
                title_font = 'Helvetica-Bold'
                title_size = 18

                # Set the content font and size
                content_font = 'Helvetica'
                content_size = 12

                # Set the title at the top of the page
                c.setFont(title_font, title_size)
                c.drawString(50, 750, title)

                # Set the content below the title
                c.setFont(content_font, content_size)

                # Calculate available width for wrapping text
                available_width = 750

                # Wrap the content text into multiple lines
                lines = textwrap.wrap(content, width=available_width//content_size)

                # Starting position for content text
                y_position = 700

                # Draw each line of the wrapped content
                for line in lines:
                    c.drawString(50, y_position, line)
                    y_position -= content_size + 5  # Adjust spacing between lines

                # Save the canvas to the PDF file
                c.save()

                print("PDF download successfuly")
            except Exception as e:
                print("PDF generation failed: ", e)

if __name__ == "__main__":
    app = QApplication([])
    window = AdminWindow()
    window.show()
    app.exec()