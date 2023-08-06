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
import textwrap

import DB.DataBase

class MessagesDataWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, "GUIui/messagesData.ui")
        uic.loadUi(UI_File_Path, self)
        self.show()

        self.presentData()

        self.exportBtn.clicked.connect(self.exportBtn_clicked)
        self.deleteBtn.clicked.connect(self.deleteBtn_clicked)
        self.viewBtn.clicked.connect(self.viewBtn_clicked)

    
    def presentData(self):
        messagesList = DB.DataBase.getMessages()

        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(["Fist Name", "Last Name", "Email", "Phone Number", "Contact Preference", "Date", "Message", "Identifier"])
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 120)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 200)
        self.tableWidget.setColumnWidth(6, 200)


        self.tableWidget.setRowCount(len(messagesList))

        i = 0
        for message in messagesList:
            self.tableWidget.setItem(i, 0, QTableWidgetItem(message['first name']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(message['last name']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(message['email']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(message['phone number']))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(message['contact preference']))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(message['Date']))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(message['content']))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(message['identifier']))

            i += 1


    def exportBtn_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Export PDF", "", "PDF files (*.pdf)")
        if filename:
            try:
                pdf = SimpleDocTemplate(filename, pagesize=landscape(A4))
                styles = getSampleStyleSheet()
                title_style = styles['Heading1']

                # Create the title paragraph
                title = Paragraph("Messages", title_style)

                # Add the title paragraph and a spacer to the document
                pdf_elements = [title, Spacer(1, 24)]

                # Convert the records into a table format
                # Add column headers
                header = ["Fist Name", "Last Name", "Email", "Phone Number", "Contact Preference", "Date", "Message"]
                data = [header]

                messagesList = DB.DataBase.getMessages()

                for message in messagesList:
                    row = [
                        message['first name'],
                        message['last name'],
                        message['email'],
                        message['phone number'],
                        message['contact preference'],
                        message['Date'],
                        message['content'],
                            ]
                    data.append(row)

                wrapped_data = []
                for row in data:
                    wrapped_row = []
                    for cell in row:
                        wrapped_cell = textwrap.wrap(cell, 300//20)
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
    
    def deleteBtn_clicked(self):
        current_row = self.tableWidget.currentRow()
        identifier = self.tableWidget.item(current_row, 7).text()
        result = DB.DataBase.deleteRecord("contact_us", identifier)
        print(identifier)
        if result:
            self.tableWidget.removeRow(current_row)

    def viewBtn_clicked(self):
        try:
            current_row = self.tableWidget.currentRow()
            identifier = self.tableWidget.item(current_row, 7).text()
            from messageView import messageViewWindow
            self.window = messageViewWindow(identifier)

        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("Please select row")
            msgBox.setWindowTitle("Something went wrong")
            msgBox.exec()
            print("no row selected: ", e)

        

if __name__ == "__main__":
    app = QApplication([])
    window = MessagesDataWindow()
    window.show()
    app.exec()