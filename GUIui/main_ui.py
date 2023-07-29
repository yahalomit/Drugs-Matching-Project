# Form implementation generated from reading ui file 'c:\Qt\bioFinal\GUIui\main.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 542)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 781, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.contactUsBtn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.contactUsBtn.setFont(font)
        self.contactUsBtn.setStyleSheet("background-color: rgb(204, 235, 207);")
        self.contactUsBtn.setObjectName("contactUsBtn")
        self.horizontalLayout.addWidget(self.contactUsBtn)
        self.adminLoginBtn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.adminLoginBtn.setFont(font)
        self.adminLoginBtn.setStyleSheet("background-color: rgb(204, 235, 207);")
        self.adminLoginBtn.setObjectName("adminLoginBtn")
        self.horizontalLayout.addWidget(self.adminLoginBtn)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 391, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.med1comboBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.med1comboBox.setFont(font)
        self.med1comboBox.setStyleSheet("background-color: rgb(235, 242, 236);")
        self.med1comboBox.setObjectName("med1comboBox")
        self.verticalLayout.addWidget(self.med1comboBox)
        self.viewBtn1 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.viewBtn1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.viewBtn1.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.viewBtn1.setFont(font)
        self.viewBtn1.setStyleSheet("background-color: rgb(225, 247, 240);")
        self.viewBtn1.setIconSize(QtCore.QSize(16, 25))
        self.viewBtn1.setObjectName("viewBtn1")
        self.verticalLayout.addWidget(self.viewBtn1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(400, 50, 391, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.med2comboBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.med2comboBox.setFont(font)
        self.med2comboBox.setStyleSheet("background-color: rgb(235, 242, 236);")
        self.med2comboBox.setIconSize(QtCore.QSize(16, 25))
        self.med2comboBox.setObjectName("med2comboBox")
        self.verticalLayout_2.addWidget(self.med2comboBox)
        self.viewBtn2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.viewBtn2.setFont(font)
        self.viewBtn2.setStyleSheet("background-color: rgb(225, 247, 240);")
        self.viewBtn2.setObjectName("viewBtn2")
        self.verticalLayout_2.addWidget(self.viewBtn2)
        self.metchBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.metchBtn.setGeometry(QtCore.QRect(10, 190, 781, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.metchBtn.setFont(font)
        self.metchBtn.setStyleSheet("background-color: rgb(204, 235, 207);")
        self.metchBtn.setObjectName("metchBtn")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 230, 781, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 781, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.mainExportBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mainExportBtn.setGeometry(QtCore.QRect(10, 400, 781, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mainExportBtn.setFont(font)
        self.mainExportBtn.setStyleSheet("background-color: rgb(204, 235, 207);")
        self.mainExportBtn.setObjectName("mainExportBtn")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 450, 621, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 450, 81, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("c:\\Qt\\bioFinal\\GUIui\\media/warining-logo.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.contactUsBtn.setText(_translate("MainWindow", "Contact Us"))
        self.adminLoginBtn.setText(_translate("MainWindow", "Admin Login"))
        self.label.setText(_translate("MainWindow", "Select Medication 1"))
        self.viewBtn1.setText(_translate("MainWindow", "View general information"))
        self.label_2.setText(_translate("MainWindow", "Select Medication 2"))
        self.viewBtn2.setText(_translate("MainWindow", "View general information"))
        self.metchBtn.setText(_translate("MainWindow", "Metch Medications"))
        self.mainExportBtn.setText(_translate("MainWindow", "Export information to PDF file"))
        self.label_3.setText(_translate("MainWindow", "All information present in this application is based on the WHO and FDA public information\n"
" in any case of taking medications it is still recommended to consult with a doctor"))