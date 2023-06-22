import pyrebase as pyrebase
from PyQt6.QtGui import QPainter

from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QTextEdit, QVBoxLayout, QFileDialog, QMessageBox

config = {
    "apiKey": "AIzaSyDM3hffm5XiESmv-mCFD8n3sWGEezV73sE",
    "authDomain": "biofinalproject-default.firebaseapp.com",
    "databaseURL": "https://biofinalproject-default-rtdb.firebaseio.com/",
    "projectId": "biofinalproject-default",
    "storageBucket": "biofinalproject-default.appspot.com",
    "messagingSenderId": "423515117698",
    "appId": "1:423515117698:web:bdc8c6c75059a7d53bfc9b",
    "measurementId": "G-L67L2PQJWQ"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()