# Form implementation generated from reading ui file 'c:\Qt\bioFinal\GUIui\messageView.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_messageViewWindow(object):
    def setupUi(self, messageViewWindow):
        messageViewWindow.setObjectName("messageViewWindow")
        messageViewWindow.resize(428, 397)
        messageViewWindow.setStyleSheet("background-color: white")
        self.centralwidget = QtWidgets.QWidget(parent=messageViewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 381, 271))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 269))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 381, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.exportBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exportBtn.setGeometry(QtCore.QRect(20, 300, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exportBtn.setFont(font)
        self.exportBtn.setStyleSheet("background-color: rgb(235, 250, 250);")
        self.exportBtn.setObjectName("exportBtn")
        messageViewWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=messageViewWindow)
        self.statusbar.setObjectName("statusbar")
        messageViewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(messageViewWindow)
        QtCore.QMetaObject.connectSlotsByName(messageViewWindow)

    def retranslateUi(self, messageViewWindow):
        _translate = QtCore.QCoreApplication.translate
        messageViewWindow.setWindowTitle(_translate("messageViewWindow", "MainWindow"))
        self.exportBtn.setText(_translate("messageViewWindow", "Export Message as PDF"))