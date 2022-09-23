from django.shortcuts import render
from firebase_config import firebase_connection

def home(request):
    database = firebase_connection()

    name = database.child('data').child('nome').get().val()
    
    context = {
        'name':name,
    }

    return render(request, "core/home.html", context)