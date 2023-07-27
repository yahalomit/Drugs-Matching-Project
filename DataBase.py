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

db = firestore.client()
batch = db.batch()

def CreateCustomToken(uid,role):
    additional_claims = {
        'role': role
    }
    auth.create_custom_token(uid, additional_claims)


def commit_batch(batch):
    try:
        batch.commit()
        return True
    except Exception as e:
        print("Batch commit failed. Error:", e)
        return False


cred = credentials.Certificate("firebase-admin-sdk.json")
firebase_admin.initialize_app(cred, {"dateBaseURL": "https://biofinalproject-default-rtdb.firebaseio.com/"})
database = pyrebase.initialize_app(config)

def createNewAdmin(firstName, lastName, ID, userName, licenseNumber, password):
    api_key =config["apiKey"]
    register_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={api_key}"

    payload = {
        "email": userName,
        "password": password,
        "returnSecureToken": True
    }

    response = requests.post(register_url, data=payload)
    result = response.json()

    if 'error' in result:
        print("Registration failed:", result['error']['message'])
        return None

    # Registration succeeded, now store additional user information
    user_id = result['localId']  # Get the user ID from the response

    # Additional user data to store
    #ref = db.reference('/')
    '''   ref.set({ 'Users':
             {
                user_id:{
                    "firstName": firstName,
                    "lastName": lastName,
                    "ID": ID,
                    "licenseNumber": licenseNumber   
                }
             }
        })'''
    data = {
        "firstName": firstName,
        "lastName": lastName,
        "ID": ID,
        "licenseNumber": licenseNumber   
    }

    database.child("Users").child(user_id).set(data)
    


    # Store the additional user data in your database or wherever you need it
    # For this example, let's just print it out
    print("Registration succeeded for user with ID:", user_id)
    print("User name:", firstName)


def signin(email, password):
        api_key = config["apiKey"]
        auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"

        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        response = requests.post(auth_url, data=payload)
        result = response.json()

        if 'error' in result:
            print("Authentication failed:", result['error']['message'])
            return False

        return True
        print("Authentication succeeded")
