import pyrebase 
from decouple import config

def firebase_connection():
    configuration = { 
        'apiKey': config("API_KEY"), 
        'authDomain': config("AUTH_DOMAIN"), 
        'databaseURL': config("DATABASE_URL"), 
        'projectId': config("PROJECT_ID"), 
        'storageBucket': config("STORAGE_BUCKET"), 
        'messagingSenderId': config("MESSAGING_SENDER_ID"), 
        'appId': config("APP_ID")
    } 

    firebase=pyrebase.initialize_app(configuration) 
    authe = firebase.auth() 
    database=firebase.database() 

    return database