# Form implementation generated from reading ui file 'c:\Qt\bioFinal\createAdmin.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_createAdminWindow(object):
    def setupUi(self, createAdminWindow):
        createAdminWindow.setObjectName("createAdminWindow")
        createAdminWindow.resize(768, 557)
        createAdminWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=createAdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 521))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.RowWrapPolicy.WrapAllRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.nameLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setStyleSheet("background-color: rgb(233, 245, 244)\n"
"")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nameLineEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lastNameLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lastNameLineEdit.setFont(font)
        self.lastNameLineEdit.setStyleSheet("background-color: rgb(233, 245, 244)\n"
"")
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lastNameLineEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.idLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.idLineEdit.setFont(font)
        self.idLineEdit.setStyleSheet("background-color: rgb(233, 245, 244)\n"
"")
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.idLineEdit)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.emailLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setStyleSheet("background-color: rgb(233, 245, 244)\n"
"")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.emailLineEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.licenseLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.licenseLineEdit.setFont(font)
        self.licenseLineEdit.setStyleSheet("background-color: rgb(233, 245, 244);")
        self.licenseLineEdit.setObjectName("licenseLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.licenseLineEdit)
        self.passwordLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet("background-color: rgb(233, 245, 244);")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_8)
        self.confPassordLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.confPassordLineEdit.setFont(font)
        self.confPassordLineEdit.setStyleSheet("background-color: rgb(233, 245, 244);")
        self.confPassordLineEdit.setObjectName("confPassordLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.confPassordLineEdit)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_7)
        self.createAdminBtn = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.createAdminBtn.setFont(font)
        self.createAdminBtn.setStyleSheet("background-color: rgb(204, 235, 207);")
        self.createAdminBtn.setObjectName("createAdminBtn")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.createAdminBtn)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 20, 351, 491))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("c:\\Qt\\bioFinal\\media/pharmacist-logo.jpg"))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_6.setObjectName("label_6")
        createAdminWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=createAdminWindow)
        self.statusbar.setObjectName("statusbar")
        createAdminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(createAdminWindow)
        QtCore.QMetaObject.connectSlotsByName(createAdminWindow)

    def retranslateUi(self, createAdminWindow):
        _translate = QtCore.QCoreApplication.translate
        createAdminWindow.setWindowTitle(_translate("createAdminWindow", "MainWindow"))
        self.label.setText(_translate("createAdminWindow", "First Name"))
        self.label_2.setText(_translate("createAdminWindow", "Last Name"))
        self.label_3.setText(_translate("createAdminWindow", "ID Number"))
        self.label_4.setText(_translate("createAdminWindow", "Email"))
        self.label_5.setText(_translate("createAdminWindow", "License number"))
        self.label_8.setText(_translate("createAdminWindow", "Confirm Password"))
        self.label_7.setText(_translate("createAdminWindow", "Password"))
        self.createAdminBtn.setText(_translate("createAdminWindow", "Create New Admin"))