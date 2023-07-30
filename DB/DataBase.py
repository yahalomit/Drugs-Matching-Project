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
        "licenseNumber": licenseNumber
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
        adminDataList.append({'First Name': a['firstName'], 'Last Name': a['lastName'], 'ID' : a['ID'], 'Email': a['email'], 'License Number': a['licenseNumber']})
    return adminDataList

def getMedicationsData():
    medicationsDataList = []
    medications_ref = DB.Config.db.collection('Medication')
    medications = medications_ref.get()
    for medications in medications:
        m = medications.to_dict()
        medicationsDataList.append({'Commertial Name': m['commertialName'], 'Generic Name': m['genericName'], 'Active Ingiridiant' : m['activeIngiridiant'],
                                     'Main Usage' : m['mainUsage'], 'Main Side Effects' : m['sideEffects'],
                                     'Allergens and Restrictions': m['allergens'], 'Menner of Cunsumption': m['cunsumption'], 'Recommended Dosage' : m['dosage'],
                                     'Menner of Storage' : m['storage']})
    return medicationsDataList


def getMedicationsNameList():
    medicationsDataList = []
    medications_ref = DB.Config.db.collection('Medication')
    medications = medications_ref.get()
    for medications in medications:
        m = medications.to_dict()
        medicationsDataList.append(m['commertialName'])
    return medicationsDataList

def getMedicationInfo(commertialName):
    medicationsDataList = []
    medications_ref = DB.Config.db.collection('Medication')
    medications = medications_ref.get()
    for medications in medications:
        m = medications.to_dict()
        if m['commertialName'] == commertialName:
            return {'Commertial Name': m['commertialName'], 'Generic Name': m['genericName'], 'Active Ingiridiant' : m['activeIngiridiant'],
                                     'Main Usage' : m['mainUsage'], 'Main Side Effects' : m['sideEffects'],
                                     'Allergens and Restrictions': m['allergens'], 'Menner of Cunsumption': m['cunsumption'], 'Recommended Dosage' : m['dosage'],
                                     'Menner of Storage' : m['storage']}
    return None