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

from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.platypus.para import Paragraph


class adminsDataWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, "GUIui/adminsData.ui")
        uic.loadUi(UI_File_Path, self)
        self.show()


        # present records chart
        self.showAdminsData()

        # activate export
        self.exportBtn.clicked.connect(self.exportPDF)

    def showAdminsData(self):
        adminsDataList = DB.DataBase.getAdminsData()

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['First Name', 'Last Name', 'ID', 'Email', 'License Number'])
        self.tableWidget.setColumnWidth(0, 152)
        self.tableWidget.setColumnWidth(1, 152)
        self.tableWidget.setColumnWidth(2, 152)
        self.tableWidget.setColumnWidth(3, 154)
        self.tableWidget.setColumnWidth(4, 152)

        self.tableWidget.setRowCount(len(adminsDataList))

        i = 0
        for admin in adminsDataList:
            self.tableWidget.setItem(i, 0, QTableWidgetItem(admin['First Name']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(admin['Last Name']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(admin['ID']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(admin['Email']))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(admin['License Number']))
            i += 1

    def exportPDF(self):
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
                header = ['First Name', 'Last Name', 'ID', 'Email', 'License Number']
                data = [header]

                adminsDataList = DB.DataBase.getAdminsData()

                for admin in adminsDataList:
                    row = [
                        admin['First Name'],
                        admin['Last Name'],
                        admin['ID'],
                        admin['Email'],
                        admin['License Number']
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
    window = adminsDataWindow()
    window.show()
    app.exec()
