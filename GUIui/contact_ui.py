# Form implementation generated from reading ui file 'c:\Qt\bioFinal\GUIui\contact.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_contactWindow(object):
    def setupUi(self, contactWindow):
        contactWindow.setObjectName("contactWindow")
        contactWindow.resize(494, 689)
        contactWindow.setStyleSheet("background-color: white")
        self.centralwidget = QtWidgets.QWidget(parent=contactWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 471, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.RowWrapPolicy.WrapLongRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.firatNamelLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.firatNamelLineEdit.setFont(font)
        self.firatNamelLineEdit.setStyleSheet("background-color: rgb(235, 242, 236);")
        self.firatNamelLineEdit.setObjectName("firatNamelLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.firatNamelLineEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lastNameLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lastNameLineEdit.setFont(font)
        self.lastNameLineEdit.setStyleSheet("background-color: rgb(235, 242, 236);")
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lastNameLineEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.emailLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setStyleSheet("background-color: rgb(235, 242, 236);")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.emailLineEdit)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.phoneLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.phoneLineEdit.setFont(font)
        self.phoneLineEdit.setStyleSheet("background-color: rgb(235, 242, 236);")
        self.phoneLineEdit.setObjectName("phoneLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.phoneLineEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 230, 471, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 469, 219))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 471, 221))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.submitBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitBtn.setGeometry(QtCore.QRect(20, 600, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.submitBtn.setFont(font)
        self.submitBtn.setStyleSheet("background-color: rgb(225, 247, 240);")
        self.submitBtn.setObjectName("submitBtn")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 470, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.emailCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.emailCheckBox.setGeometry(QtCore.QRect(220, 550, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.emailCheckBox.setFont(font)
        self.emailCheckBox.setObjectName("emailCheckBox")
        self.phoneCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.phoneCheckBox.setGeometry(QtCore.QRect(350, 550, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.phoneCheckBox.setFont(font)
        self.phoneCheckBox.setObjectName("phoneCheckBox")
        contactWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=contactWindow)
        self.statusbar.setObjectName("statusbar")
        contactWindow.setStatusBar(self.statusbar)

        self.retranslateUi(contactWindow)
        QtCore.QMetaObject.connectSlotsByName(contactWindow)

    def retranslateUi(self, contactWindow):
        _translate = QtCore.QCoreApplication.translate
        contactWindow.setWindowTitle(_translate("contactWindow", "MainWindow"))
        self.label.setText(_translate("contactWindow", "First Name"))
        self.label_2.setText(_translate("contactWindow", "Last Name"))
        self.label_3.setText(_translate("contactWindow", "Email"))
        self.label_4.setText(_translate("contactWindow", "Phone Number"))
        self.label_5.setText(_translate("contactWindow", "What\'s on Your Mind?"))
        self.submitBtn.setText(_translate("contactWindow", "Submit"))
        self.label_6.setText(_translate("contactWindow", "We will do are best to contact you as soon as possible,\n"
" do you have preference how ?\n"
"skip the selection of not"))
        self.emailCheckBox.setText(_translate("contactWindow", "By Email"))
        self.phoneCheckBox.setText(_translate("contactWindow", "By Phone"))