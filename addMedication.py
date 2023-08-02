# Yahalomit Levi 203956321
# Nisan Fichman 204470199

import os
import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QPushButton,QComboBox,QMessageBox, QFileDialog
from PyQt6.QtCore import Qt,QRunnable, QThreadPool, QDate, QTime, QDateTime, QFileInfo
from PyQt6 import uic, QtGui
from PyQt6.QtGui import QPixmap, QTextCursor

import DB.DataBase

class addMedicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        script_path = os.path.dirname(os.path.realpath(__file__))
        UI_File_Path = os.path.join(script_path, "GUIui/addMedication.ui")
        uic.loadUi(UI_File_Path, self)
        self.show()

        self.cunsumptionComboBox.addItem("Oral")
        self.cunsumptionComboBox.addItem("Anal")
        self.cunsumptionComboBox.addItem("Vaginal")
        self.cunsumptionComboBox.addItem("Dermal")
        self.cunsumptionComboBox.addItem("Through the Ears")
        self.cunsumptionComboBox.addItem("Through the Eyes")
        self.cunsumptionComboBox.addItem("Sublingual")
        self.cunsumptionComboBox.addItem("Through the Nose")
        self.cunsumptionComboBox.addItem("Rectal")
        self.cunsumptionComboBox.addItem("Through the Muscle")
        

        self.typeComboBox.addItem("Capsule")
        self.typeComboBox.addItem("Pill")
        self.typeComboBox.addItem("Tablet")
        self.typeComboBox.addItem("Chewable Tablet")
        self.typeComboBox.addItem("Spry")
        self.typeComboBox.addItem("Drops")
        self.typeComboBox.addItem("Lotion")
        self.typeComboBox.addItem("Inhalers")
        self.typeComboBox.addItem("Injections")
        self.typeComboBox.addItem("Patches")
        self.typeComboBox.addItem("Suspension")

        pixmap = QPixmap("media/drugs2.jpg")
        self.label_10.setPixmap(pixmap)

        self.submitBtn.clicked.connect(self.submitBtn_clicked)
    
    def submitBtn_clicked(self):
        if self.genricNameLineEdit.text() and self.commertialNameLineEdit.text() and self.activeIngridiantLineEdit.text() and self.cunsumptionComboBox.currentText()\
        and self.typeComboBox.currentText() and self.dosageLineEdit.text() and self.mainUsageLineEdit.text() and self.storageLineEdit.text() and self.textEdit_3.toPlainText()\
        and self.textEdit_4.toPlainText():
            if DB.DataBase.checkMedicationData(str(self.commertialNameLineEdit.text())):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("Commertial name already exist")
                msgBox.setWindowTitle("Something went wrong")
                msgBox.exec()
            else:
                DB.DataBase.addMedicationToDB(str(self.genricNameLineEdit.text()), str(self.commertialNameLineEdit.text()), str(self.activeIngridiantLineEdit.text()),
                                               str(self.cunsumptionComboBox.currentText()), str(self.typeComboBox.currentText()), str(self.dosageLineEdit.text()),
                                               str( self.mainUsageLineEdit.text()), str(self.storageLineEdit.text()), str(self.textEdit_3.toPlainText()),
                                               str(self.textEdit_4.toPlainText()))                
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("There are missing fields")
            msgBox.setWindowTitle("Something went wrong")
            msgBox.exec()
    
    def handle_text_changed(self):
        self.max_rows = 10  # Maximum number of rows
        self.max_line_length = 30  # Maximum line length
    
        cursor1 = self.textEdit_3.textCursor()
        lines1 = self.textEdit_3.toPlainText().split('\n')

        cursor2 = self.textEdit_3.textCursor()
        lines2 = self.textEdit_3.toPlainText().split('\n')

        # Check number of rows
        if len(lines1) > self.max_rows:
            cursor1.movePosition(QTextCursor.End, QTextCursor.MoveMode.KeepAnchor)
            cursor1.insertText("\b")  # Delete the last character to prevent exceeding max rows
        if len(lines2) > self.max_rows:           
            cursor2.movePosition(QTextCursor.End, QTextCursor.MoveMode.KeepAnchor)
            cursor2.insertText("\b")  # Delete the last character to prevent exceeding max rows

        # Check line length
        if any(len(line) > self.max_line_length for line in lines1):
            cursor1.movePosition(QTextCursor.StartOfBlock, QTextCursor.MoveMode.KeepAnchor)
            cursor1.movePosition(QTextCursor.EndOfBlock, QTextCursor.MoveMode.KeepAnchor)
            selected_text1 = cursor1.selectedText()
            if len(selected_text1) > self.max_line_length:
                cursor1.removeSelectedText()
        if any(len(line) > self.max_line_length for line in lines):
            cursor2.movePosition(QTextCursor.StartOfBlock, QTextCursor.MoveMode.KeepAnchor)
            cursor2.movePosition(QTextCursor.EndOfBlock, QTextCursor.MoveMode.KeepAnchor)
            selected_text2 = cursor2.selectedText()
            if len(selected_text2) > self.max_line_length:
                cursor2.removeSelectedText()



if __name__ == "__main__":
    app = QApplication([])
    window = addMedicationWindow()
    window.show()
    app.exec()