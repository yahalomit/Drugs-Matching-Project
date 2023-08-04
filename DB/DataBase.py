import DB.Config

def createNewAdmin(firstName, lastName, ID, email, licenseNumber, password):
    api_key = DB.Config.config["apiKey"]
    register_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={api_key}"

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = DB.Config.requests.post(register_url, data=payload)
    result = response.json()

    if 'error' in result:
        print("Registration failed:", result['error']['message'])
        return 'error: ' + result['error']['message']

    # Registration succeeded, now store additional user information
    user_id = result['localId']  # Get the user ID from the response

    # Additional user data to store

    user_data = {
        "firstName": firstName,
        "lastName": lastName,
        "ID": ID,
        "licenseNumber": licenseNumber,
        "email": email
    }

    users_ref = DB.Config.db.collection("Users").document(user_id)
    users_ref.set(user_data)
    return None

    # Store the additional user data in your database or wherever you need it
    # For this example, let's just print it out
    print("Registration succeeded for user with ID:", user_id)
    print("User name:", firstName)


def checkAdminData(ID, licenseNumber):
    admins_ref = DB.Config.db.collection('Users')
    admins = admins_ref.get()
    for admin in admins:
        a = admin.to_dict()
        if a['ID'] == ID:
            return 'ID'
        elif a['licenseNumber'] == licenseNumber:
            return 'license number'
    return True

def signin(email, password):
    api_key = DB.Config.config["apiKey"]
    auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = DB.Config.requests.post(auth_url, data=payload)
    result = response.json()

    if 'error' in result:
        print("Authentication failed:", result['error']['message'])
        return None
    
    user_id = result['localId']  # Get the user ID from the response
    users_ref = DB.Config.db.collection("Users").document(user_id)
    user = DB.Config.db.collection("Users").document(user_id).get()
    user_name = user.to_dict()['firstName'] + " " + user.to_dict()['lastName']
    print("Authentication succeeded")
    return user_name

def getAdminsData():
    adminDataList = []
    admins_ref = DB.Config.db.collection('Users')
    admins = admins_ref.get()
    for admin in admins:
        a = admin.to_dict()
        print(a)
        adminDataList.append({'First Name': a['firstName'], 'Last Name': a['lastName'], 'ID' : a['ID'], 'Email': a['email'], 'License Number': a['licenseNumber']})
    return adminDataList

def getMedicationsData():
    medicationsDataList = []
    medications_ref = DB.Config.db.collection('Medications')
    medications = medications_ref.get()
    for medications in medications:
        m = medications.to_dict()
        medicationsDataList.append({'Commertial Name': m['Commertial Name'], 'Generic Name': m['Generic Name'], 'Active Ingiridiant' : m['Active Ingridiant'],
                                     'Main Usage' : m['Main Usage'], 'Main Side Effects' : m['Main Side Effects'], 'Medication Type' : m['Medication TYpe'],
                                     'Allergens and Restrictions': m['Allergens and\n Restrictions'], 'Menner of Cunsumption': m['Manner of Cunsumption'],
                                     'Recommended Dosage' : m['Recommended Dosage'], 'Menner of Storage' : m['Storage']})
    return medicationsDataList


def getMedicationsNameList():
    medicationsDataList = []
    medications_ref = DB.Config.db.collection('Medications')
    medications = medications_ref.get()
    for medications in medications:
        m = medications.to_dict()
        medicationsDataList.append(m['Commertial Name'])
    return medicationsDataList

def getMedicationInfo(commertialName):
    medicationsDataList = []
    medications_ref = DB.Config.db.collection('Medications')
    medications = medications_ref.get()
    for medications in medications:
        m = medications.to_dict()
        if m['Commertial Name'] == commertialName:
            return {'Commertial Name': m['Commertial Name'], 'Generic Name': m['Generic Name'], 'Active Ingiridiant' : m['Active Ingridiant'],
                                     'Main Usage' : m['Main Usage'], 'Main Side Effects' : m['Main Side Effects'], 'Medication Type' : m['Medication TYpe'],
                                     'Allergens and Restrictions': m['Allergens and\n Restrictions'], 'Manner of Cunsumption': m['Manner of Cunsumption'],
                                     'Recommended Dosage' : m['Recommended Dosage'], 'Menner of Storage' : m['Storage']}
    return None

def saveContactLettersToDB(firstName, lastName, email, phoneNumber, letter, contactPreference):
    today = DB.Config.date.today()
    contact_id = DB.Config.random.randint(100000,999999)

    letter_data = {
        "first name": firstName,
        "last name": lastName,
        "email": email,
        "phone number": phoneNumber,
        "content" : letter,
        "contact preference": contactPreference,
        "Date" : str(today),
        'identifier': str(contact_id)
    }

    contact_ref = DB.Config.db.collection("contact_us").document(str(contact_id))
    contact_ref.set(letter_data)


def getMessages():
    messagesDataList = []
    messages_ref = DB.Config.db.collection('contact_us')
    messages = messages_ref.get()
    for message in messages:
        m = message.to_dict()
        messagesDataList.append(m)
    return messagesDataList


def addMedicationToDB(genericName, commertialName, activeIngriant, cunsumption,type, dosage,mainUsage,storage,sideEffects, allergansAndRestrictions):
    medicationData = {
        "Generic Name": genericName,
        "Commertial Name": commertialName,
        "Active Ingridiant": activeIngriant,
        "Manner of Cunsumption": cunsumption,
        "Medication TYpe": type,
        "Recommended Dosage" : dosage,
        "Main Usage": mainUsage,
        "Storage" : storage,
        "Main Side Effects":sideEffects,
        "Allergens and\n Restrictions":allergansAndRestrictions

    }

    contact_ref = DB.Config.db.collection("Medications").document(str(commertialName))
    contact_ref.set(medicationData)

def checkMedicationData(commertialName):
    medication_ref = DB.Config.db.collection('Medication')
    medications = medication_ref.get()
    for medication in medications:
        m = medication.to_dict()
        if m['commertialName'] == commertialName:
            return True
    return False

def getMedicationData():
    medicationsDataList = []
    medications_ref = DB.Config.db.collection('Medications')
    medications = medications_ref.get()
    for medication in medications:
        m = medication.to_dict()
        medicationsDataList.append(m)
    return medicationsDataList

def deleteRecordMed(collection, identifier):
    doc_ref = DB.Config.db.collection(collection).document(identifier)
    doc = doc_ref.get()
    print(doc)
    if doc.exists:
        print(f"Document {doc.id} exists, deleting it now...")
        doc_ref.delete()
        print(f"Document {doc.id} deleted successfully.")
    else:
        print(f"Document {doc.id} does not exist.")

def deleteRecord(collection, identifier):
        query = DB.Config.db.collection(collection).where("identifier" ,"==", identifier)
        docs = query.stream()
        for doc in docs:
            doc.reference.delete()
            return True
        return False

def delete_admin_record(email):

    user = DB.Config.auth.get_user_by_email(email)
    user_id = user.uid

    try:
        # Delete the user authentication data
        DB.Config.auth.delete_user(user_id)

        # Delete the user record from the "Users" collection
        users_ref = DB.Config.db.collection("Users").document(user_id)
        users_ref.delete()

        print("User record and authentication data deleted successfully!")
        return False
    except Exception as e:
        print("Error deleting user record and authentication data:", e)
        return str(e)
    

def metchMedications(commertialName1, commertialName2):
    doc_ref1 = DB.Config.db.collection("Medications").document(commertialName1)
    doc_ref2 = DB.Config.db.collection("Medications").document(commertialName2)
    doc1 = doc_ref1.get().to_dict()
    doc2 = doc_ref2.get().to_dict()
    contradictions_ref = DB.Config.db.collection("contradiction")
    contradictions = contradictions_ref.get()
    if 'Charcoal activated' in doc2['Active Ingridiant'] or  'Charcoal activated' in doc1['Active Ingridiant']:
        doc_ref = DB.Config.db.collection('contradiction').document('9rnwtlJddEcXY0ECw9fr')
        doc = doc_ref.get().to_dict()
        return doc['contradiction']
    for contradiction in contradictions:
        c = contradiction.to_dict()
        if  ( c['component1'] in doc1['Active Ingridiant'] and c['component2'] in doc2['Active Ingridiant'])\
            or (c['component1'] in doc2['Active Ingridiant'] and c['component2'] in doc1['Active Ingridiant']):
            return c['contradiction'] 
    return None