# Yahalomit Levi 203956321
# Nisan Fichman 204470199

import os
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QPushButton,QComboBox,QMessageBox, QFileDialog
from PyQt6.QtCore import Qt,QRunnable, QThreadPool, QDate, QTime, QDateTime, QFileInfo
from PyQt6 import uic, QtGui

from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.platypus.para import Paragraph

import DB.DataBase

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class AdminDataWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, resource_path("GUIui/adminData.ui"))
        uic.loadUi(UI_File_Path, self)
        self.show()

        self.presentData()

        self.exportButton.clicked.connect(self.exportButton_clicked)
    
    def presentData(self):
        adminsList = DB.DataBase.getAdminsAsList()

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Email", "Fist Name", "Last Name", "License Number"])
        self.tableWidget.setColumnWidth(0, 154)
        self.tableWidget.setColumnWidth(1, 155)
        self.tableWidget.setColumnWidth(2, 155)
        self.tableWidget.setColumnWidth(3, 155)
        self.tableWidget.setColumnWidth(4, 155)

        self.tableWidget.setRowCount(len(adminsList))

        i = 0
        for admin in adminsList:
            self.tableWidget.setItem(i, 0, QTableWidgetItem(admin[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(admin[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(admin[2]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(admin[3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(admin[4]))
            i += 1


    def exportButton_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Export PDF", "", "PDF files (*.pdf)")
        if filename:
            try:
                pdf = SimpleDocTemplate(filename, pagesize=landscape(A4))
                styles = getSampleStyleSheet()
                title_style = styles['Heading1']

                # Create the title paragraph
                title = Paragraph("Admins", title_style)

                # Add the title paragraph and a spacer to the document
                pdf_elements = [title, Spacer(1, 24)]

                # Convert the records into a table format
                # Add column headers
                header = ["ID", "Email", "Fist Name", "Last Name", "License Number"]
                data = [header]

                Admin_list = DB.DataBase.getAdminsAsList()

                for admin in Admin_list:
                    row = [
                        admin[0],
                        admin[1],
                        admin[2],
                        admin[3],
                        admin[4]
                            ]
                    data.append(row)

                table = Table(data)
                table.colWidths = [100, 70, 80, 100, 80, 80, 100, 80]

                # Apply table styles
                table.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),

                            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                            ("FONTSIZE", (0, 0), (-1, 0), 14),

                            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                            ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                            ("GRID", (0, 0), (-1, -1), 1, colors.black),
                            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                            ("FONTSIZE", (0, 1), (-1, -1), 12),
                        ]
                    )
                )

                pdf_elements.append(table)

                pdf.build(pdf_elements)
                print("pdf export complete successfully")
            except Exception as e:
                print("PDF generation failed: ", e)

if __name__ == "__main__":
    app = QApplication([])
    window = AdminDataWindow()
    window.show()
    app.exec()