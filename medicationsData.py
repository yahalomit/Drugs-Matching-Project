# Yahalomit Levi 203956321
# Nisan Fichman 204470199

import os
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QTableWidgetItem, QMessageBox
from PyQt6 import uic


import DB.DataBase

from reportlab.lib.pagesizes import landscape, A1
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.platypus.para import Paragraph
import textwrap


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class medicationsDataWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, resource_path("GUIui/medicationsData.ui"))
        uic.loadUi(UI_File_Path, self)
        self.show()

        # present records chart
        self.showMedicationsData()

        # activate export
        self.exportBtn.clicked.connect(self.exportPDF)
        self.deleteBtn.clicked.connect(self.deleteBtn_clicked)
        self.viewBtn.clicked.connect(self.viewBtn_clicked)


    def showMedicationsData(self):
        
        MedicationsDataList = DB.DataBase.getMedicationsData()

        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(['Commertial Name', 'Generic Name', 'Active Ingiridiant','Main Usage', 'Main Side Effects',
                                     'Allergens and Restrictions', 'Menner of Cunsumption', 'Recommended Dosage','Menner of Storage'])
        for i in range(10):
            self.tableWidget.setColumnWidth(i, 150)


        self.tableWidget.setRowCount(len(MedicationsDataList))
        
        i=0
        for medication in MedicationsDataList:
            self.tableWidget.setItem(i, 0, QTableWidgetItem(medication['Commertial Name']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(medication['Generic Name']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(medication['Active Ingiridiant']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(medication['Main Usage']))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(medication['Main Side Effects']))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(medication['Allergens and Restrictions']))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(medication['Menner of Cunsumption']))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(medication['Medication Type']))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(medication['Recommended Dosage']))
            self.tableWidget.setItem(i, 9, QTableWidgetItem(medication['Menner of Storage']))
            i+=1

    
    def exportPDF(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Export PDF", "", "PDF files (*.pdf)")
        if filename:
            try:
                pdf = SimpleDocTemplate(filename, pagesize=landscape(A1))
                styles = getSampleStyleSheet()
                title_style = styles['Heading1']

                # Create the title paragraph
                title = Paragraph("Medications", title_style)

                # Add the title paragraph and a spacer to the document
                pdf_elements = [title, Spacer(1, 24)]

                # Convert the records into a table format
                # Add column headers
                header = ['Commertial Name', 'Generic Name', 'Active Ingiridiant','Main Usage', 'Main Side Effects',
                                     'Allergens and Restrictions', 'Menner of Cunsumption', 'Recommended Dosage','Menner of Storage']
                data = [header]

                MedicationsDataList = DB.DataBase.getMedicationsData()

                for medication in MedicationsDataList:
                    row = [
                        medication['Commertial Name'],
                        medication['Generic Name'],
                        medication['Active Ingiridiant'],
                        medication['Main Usage'],
                        medication['Main Side Effects'],
                        medication['Allergens and Restrictions'],
                        medication['Menner of Cunsumption'],
                        medication['Recommended Dosage'],
                        medication['Menner of Storage'],
                            ]
                    data.append(row)

                wrapped_data = []
                for row in data:
                    wrapped_row = []
                    for cell in row:
                        wrapped_cell = textwrap.wrap(cell, 300//7)
                        wrapped_row.append('\n'.join(wrapped_cell))
                    wrapped_data.append(wrapped_row)


                # Calculate the available page width
                available_page_width = pdf.width

                # Calculate the width for each column based on the available page width
                num_columns = len(header)
                column_width = available_page_width / num_columns

                table = Table(wrapped_data, colWidths=[column_width]*num_columns)  # Adjust the width of each column


                # Apply table styles
                table.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),

                            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                            ("FONTSIZE", (0, 0), (-1, 0), 11),

                            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                            ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                            ("GRID", (0, 0), (-1, -1), 1, colors.black),
                            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                            ("FONTSIZE", (0, 1), (-1, -1), 9),
                        ]
                    )
                )

                pdf_elements.append(table)

                pdf.build(pdf_elements)
                print("pdf export complete successfully")

            except Exception as e:
                print("PDF generation failed: ", e)



    def deleteBtn_clicked(self):
        current_row = self.tableWidget.currentRow()
        CommertialName = self.tableWidget.item(current_row, 0).text()
        print(CommertialName)
        result = DB.DataBase.deleteRecordMed("Medications", CommertialName)
        if result:
            self.tableWidget.removeRow(current_row)
    
    def viewBtn_clicked(self):
        try:
            current_row = self.tableWidget.currentRow()
            CommertialName = self.tableWidget.item(current_row, 0).text()
            from generalInfo import generalInfoWindow
            self.window = generalInfoWindow(CommertialName)

        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("Please select row")
            msgBox.setWindowTitle("Something went wrong")
            msgBox.exec()
            print("no row selected: ", e)


if __name__ == "__main__":
    app = QApplication([])
    window = medicationsDataWindow()
    window.show()
    app.exec()