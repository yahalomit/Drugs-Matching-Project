# Form implementation generated from reading ui file 'c:\Qt\bioFinal\GUIui\medicationsData.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_medicationsDataWindow(object):
    def setupUi(self, medicationsDataWindow):
        medicationsDataWindow.setObjectName("medicationsDataWindow")
        medicationsDataWindow.resize(798, 491)
        self.centralwidget = QtWidgets.QWidget(parent=medicationsDataWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 771, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 781, 211))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 209))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 781, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.exportBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exportBtn.setGeometry(QtCore.QRect(20, 290, 761, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exportBtn.setFont(font)
        self.exportBtn.setStyleSheet("background-color: rgb(235, 250, 250);")
        self.exportBtn.setObjectName("exportBtn")
        self.deleteBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(20, 350, 761, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setStyleSheet("background-color: rgb(235, 250, 250);")
        self.deleteBtn.setObjectName("deleteBtn")
        self.viewBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.viewBtn.setGeometry(QtCore.QRect(20, 410, 761, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.viewBtn.setFont(font)
        self.viewBtn.setStyleSheet("background-color: rgb(235, 250, 250);")
        self.viewBtn.setObjectName("viewBtn")
        medicationsDataWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=medicationsDataWindow)
        self.statusbar.setObjectName("statusbar")
        medicationsDataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(medicationsDataWindow)
        QtCore.QMetaObject.connectSlotsByName(medicationsDataWindow)

    def retranslateUi(self, medicationsDataWindow):
        _translate = QtCore.QCoreApplication.translate
        medicationsDataWindow.setWindowTitle(_translate("medicationsDataWindow", "MainWindow"))
        self.label.setText(_translate("medicationsDataWindow", "Medications Data"))
        self.exportBtn.setText(_translate("medicationsDataWindow", "Export Data to PDF File"))
        self.deleteBtn.setText(_translate("medicationsDataWindow", "Delete Record"))
        self.viewBtn.setText(_translate("medicationsDataWindow", "View Current Mediction data"))
