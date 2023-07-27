from PyQt6.QtGui import QPainter
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QTextEdit, QVBoxLayout, QFileDialog, QMessageBox
from datetime import date

import firebase_admin
from firebase_admin import credentials, db, auth, firestore
import bcrypt
import requests

config = {
    'apiKey': "AIzaSyAKjdX4I05qFIoT5r0wgWsSw4YvBID1PyY",
    'authDomain': "biofinalproject.firebaseapp.com",
    'databaseURL': "https://biofinalproject-default-rtdb.firebaseio.com",
    'projectId': "biofinalproject",
    'storageBucket': "biofinalproject.appspot.com",
    'messagingSenderId': "1045599140915",
    'appId': "1:1045599140915:web:d71d67e46b8b009c807746",
    'measurementId': "G-4D9R8TMFR1"
}


cred = credentials.Certificate("firebase-admin-sdk.json")
firebase_admin.initialize_app(cred, {"dateBaseURL": "https://biofinalproject-default-rtdb.firebaseio.com/"})
db = firestore.client()