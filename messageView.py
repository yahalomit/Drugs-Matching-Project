import os
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt6 import uic
import DB.DataBase

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.platypus.para import Paragraph
import textwrap

class messageViewWindow(QMainWindow):
    def __init__(self, identifier):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, "GUIui/messageView.ui")
        uic.loadUi(UI_File_Path, self)
        self.show()

        self.identifier = identifier

        self.exportBtn.clicked.connect(self.exportBtn_clicked)

        self.showLetter(identifier)
    
    def showLetter(self,identifier):
        data = DB.DataBase.getMessageData(identifier)
        if data==None:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("Message was no found")
            msgBox.setWindowTitle("Something went wrong")
            msgBox.exec()
        else:
            print(data)
            for d in data:
                self.textBrowser.append(d + " : " + data[d])

    def exportBtn_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Export PDF", "", "PDF files (*.pdf)")
        information = DB.DataBase.getMessageData(self.identifier)
        if filename:
            try:
                pdf = SimpleDocTemplate(filename, pagesize=landscape(letter))
                styles = getSampleStyleSheet()
                title_style = styles['Heading1']

                # Create the title paragraph
                title = Paragraph(self.identifier, title_style)

                # Add the title paragraph and a spacer to the document
                pdf_elements = [title, Spacer(1, 24)]

                # Convert the records into a table format
                # Add column headers
                header = [" ", "    ", "    ", "    ", "    ", "    ", "    ", "    "]
                data = [header]

                record_list = DB.DataBase.getMedicationInfo(self.identifier)

                data.append(["Identifier : ", information["identifier"]])
                data.append(["Fist Name : ", information["first name"]])
                data.append(["Last Name : ", information["last name"]])
                data.append(["Email : ", information["email"]])
                data.append(["Phone Number : ", information["phone number"]])
                data.append(["Contact Preference : ", information["contact preference"]])
                data.append(["Date : " , information["Date"]])
                data.append(["Message : " , information["content"]])


                # Create the table with the modified table_data
                wrapped_data = []
                for row in data:
                    wrapped_row = []
                    for cell in row:
                        wrapped_cell = textwrap.wrap(cell, 450//5)
                        wrapped_row.append('\n'.join(wrapped_cell))
                    wrapped_data.append(wrapped_row)


                # Calculate the available page width
                available_page_width = pdf.width

                # Calculate the width for each column based on the available page width
                num_columns = len(header)
                column_width = available_page_width / num_columns

                table = Table(wrapped_data, colWidths=[column_width]*num_columns)  # Adjust the width of each column

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
    window = messageViewWindow('acamol')
    window.show()
    app.exec()