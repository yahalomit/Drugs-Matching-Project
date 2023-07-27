import DB.Config

def createNewAdmin(firstName, lastName, ID, userName, licenseNumber, password):
    api_key = DB.Config.config["apiKey"]
    register_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={api_key}"

    payload = {
        "email": userName,
        "password": password,
        "returnSecureToken": True
    }

    response = DB.Config.requests.post(register_url, data=payload)
    result = response.json()

    if 'error' in result:
        print("Registration failed:", result['error']['message'])
        return None

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


    # Store the additional user data in your database or wherever you need it
    # For this example, let's just print it out
    print("Registration succeeded for user with ID:", user_id)
    print("User name:", firstName)


'''def signin(email, password):
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
        return False

    return True
    print("Authentication succeeded")'''

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

