from django.shortcuts import render
import firebase_config

def home(request):
    people = []

    dbconn = firebase_config.connectDB("Person")
    tblPeople = dbconn.get()

    for key, value in tblPeople.items():
        for k, v in value.items():
            people.append({k:v})

    #firebase_config.push("silas")

    return render(request, "core/home.html", {'people':people})