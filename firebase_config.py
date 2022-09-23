import pyrebase 
import firebase_admin
from decouple import config
from firebase_admin import credentials
from firebase_admin import db

def connectDB(data):
    if not firebase_admin._apps:
        cred = credentials.Certificate("firebase-key.json")
        firebase_admin.initialize_app(cred, {
            "databaseURL": config('DATABASE_URL')
        })
    dbconn = db.reference(data)
    return dbconn

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

def push(data):
    if not firebase_admin._apps:
        cred = credentials.Certificate("firebase-key.json")
        firebase_admin.initialize_app(cred, {
            "databaseURL": config('DATABASE_URL')
        })

    dbref = db.reference("Person")

    dbref.push({"nome": data})
