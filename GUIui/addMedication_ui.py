# Form implementation generated from reading ui file 'c:\Qt\bioFinal\GUIui\addMedication.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_addMedWindow(object):
    def setupUi(self, addMedWindow):
        addMedWindow.setObjectName("addMedWindow")
        addMedWindow.resize(714, 663)
        addMedWindow.setStyleSheet("background-color:rgb(255,255,255)")
        self.centralwidget = QtWidgets.QWidget(parent=addMedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 691, 430))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.genricNameLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.genricNameLineEdit.setFont(font)
        self.genricNameLineEdit.setStyleSheet("background-color:rgb(233, 245, 244)")
        self.genricNameLineEdit.setObjectName("genricNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.genricNameLineEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.commertialNameLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commertialNameLineEdit.setFont(font)
        self.commertialNameLineEdit.setStyleSheet("background-color:rgb(233, 245, 244)")
        self.commertialNameLineEdit.setObjectName("commertialNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.commertialNameLineEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.activeIngridiantLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.activeIngridiantLineEdit.setFont(font)
        self.activeIngridiantLineEdit.setStyleSheet("background-color:rgb(233, 245, 244)")
        self.activeIngridiantLineEdit.setObjectName("activeIngridiantLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.activeIngridiantLineEdit)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.cunsumptionComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cunsumptionComboBox.setFont(font)
        self.cunsumptionComboBox.setStyleSheet("background-color:rgb(247, 255, 247);")
        self.cunsumptionComboBox.setObjectName("cunsumptionComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cunsumptionComboBox)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.dosageLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dosageLineEdit.setFont(font)
        self.dosageLineEdit.setStyleSheet("background-color:rgb(233, 245, 244)")
        self.dosageLineEdit.setObjectName("dosageLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dosageLineEdit)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.mainUsageLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mainUsageLineEdit.setFont(font)
        self.mainUsageLineEdit.setStyleSheet("background-color:rgb(233, 245, 244)")
        self.mainUsageLineEdit.setObjectName("mainUsageLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.mainUsageLineEdit)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.storageLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.storageLineEdit.setFont(font)
        self.storageLineEdit.setStyleSheet("background-color:rgb(233, 245, 244)")
        self.storageLineEdit.setObjectName("storageLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.storageLineEdit)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.formLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 479, 69))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents_3)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("background-color:rgb(247, 255, 247);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.formLayoutWidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 479, 69))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.textEdit_4 = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents_4)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 0, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("background-color:rgb(247, 255, 247);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.scrollArea_2)
        self.label_11 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.typeComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.typeComboBox.setFont(font)
        self.typeComboBox.setStyleSheet("background-color:rgb(247, 255, 247);")
        self.typeComboBox.setObjectName("typeComboBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.typeComboBox)
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 450, 351, 191))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("c:\\Qt\\bioFinal\\GUIui\\media/pharmeci-logo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.submitBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitBtn.setGeometry(QtCore.QRect(390, 450, 311, 201))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.submitBtn.setFont(font)
        self.submitBtn.setStyleSheet("background-color: rgb(204, 235, 207);")
        self.submitBtn.setObjectName("submitBtn")
        addMedWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=addMedWindow)
        self.statusbar.setObjectName("statusbar")
        addMedWindow.setStatusBar(self.statusbar)

        self.retranslateUi(addMedWindow)
        QtCore.QMetaObject.connectSlotsByName(addMedWindow)

    def retranslateUi(self, addMedWindow):
        _translate = QtCore.QCoreApplication.translate
        addMedWindow.setWindowTitle(_translate("addMedWindow", "MainWindow"))
        self.label.setText(_translate("addMedWindow", "Generic Name"))
        self.label_2.setText(_translate("addMedWindow", "Commertial Name"))
        self.label_3.setText(_translate("addMedWindow", "Active Ingridiant"))
        self.label_4.setText(_translate("addMedWindow", "Manner of Cunsumption"))
        self.label_5.setText(_translate("addMedWindow", "Recommended Dosage"))
        self.label_6.setText(_translate("addMedWindow", "Main Usage"))
        self.label_8.setText(_translate("addMedWindow", "Storage"))
        self.label_7.setText(_translate("addMedWindow", "Main Side Effects"))
        self.label_9.setText(_translate("addMedWindow", "Allergens and\n"
" Restrictions"))
        self.label_11.setText(_translate("addMedWindow", "Medication Type"))
        self.submitBtn.setText(_translate("addMedWindow", "Submit"))
