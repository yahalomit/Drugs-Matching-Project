# Yahalomit Levi 203956321
# Nisan Fichman 204470199

from datetime import datetime
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
        self.viewInfoButton.clicked.connect(self.viewInfoButton_clicked)
        self.exportBtn.clicked.connect(self.exportBtn_clicked)

        self.actionCreate_new_Admin.triggered.connect(self.action_Create_new_Admin)
        self.actionView_All_Admins_Data.triggered.connect(self.action_View_All_Admins_Data)
        self.actionView_All_Medication_Data.triggered.connect(self.action_View_All_Medication_Data)

        medicationsNameList = DB.DataBase.getMedicationsNameList()

        for medication in medicationsNameList:
            self.medComboBox.addItem(medication)


    def action_View_All_Medication_Data(self):
        from medicationsData import medicationsDataWindow
        self.window = medicationsDataWindow()


    def action_View_All_Admins_Data(self):
        from adminsData import adminsDataWindow
        self.window = adminsDataWindow()

    def clicked_logout(self):
        from login import LoginWindow
        self.window = LoginWindow()
        self.close()

    def action_Create_new_Admin(self):
        from createAdmin import createAdminWindow
        self.window = createAdminWindow()

    def viewInfoButton_clicked(self):
        self.textBrowser.clear()
        information = DB.DataBase.getMedicationInfo(str(self.medComboBox.currentText()))
        if information != None:
            for info in information:
                self.textBrowser.append(info + " : " + information[info])

    def exportBtn_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Export PDF", "", "PDF files (*.pdf)")
        medName = str(self.medComboBox.currentText())
        information = DB.DataBase.getMedicationInfo(str(self.medComboBox.currentText()))
        if filename:
            try:
                pdf = SimpleDocTemplate(filename, pagesize=landscape(A4))
                styles = getSampleStyleSheet()
                title_style = styles['Heading1']

                # Create the title paragraph
                title = Paragraph(medName, title_style)

                # Add the title paragraph and a spacer to the document
                pdf_elements = [title, Spacer(1, 24)]

                # Convert the records into a table format
                # Add column headers
                header = ["Blood Type", "Donation Date", "First Name", "Last Name", "ID"]
                data = [header]

                record_list = DB.DataBase.getMedicationInfo(medName)

                # Create a list to hold the table data
                table_data = []

                # Add each key-value pair to the table_data list as separate rows
                for key, value in information.items():
                    table_data.append([f"{key}:", value])

                # Create the table with the modified table_data
                table = Table(table_data)
                table.colWidths = [100, 70, 80, 100, 80, 80, 100, 80]

                # Apply table styles
                table_style = TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Gray background for header row
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # White text for header row
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Left-align all cells
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header row
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Add padding to the header row
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Background color for data rows
                ])

                table.setStyle(table_style)


                pdf_elements.append(table)

                pdf.build(pdf_elements)
                print("pdf export complete successfully")
            except Exception as e:
                print("PDF generation failed: ", e)

if __name__ == "__main__":
    app = QApplication([])
    window = AdminWindow('Shay Ginsburg')
    window.show()
    app.exec()