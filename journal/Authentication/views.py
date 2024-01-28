from django.shortcuts import render, redirect
from django.contrib import messages
from HomePage.views import *
import pyrebase
from django.http import HttpResponseRedirect
# from requests.exceptions import HTTPError

firebaseConfig = {
  "apiKey": "AIzaSyAFNwVq9PhFxystAc3vk-hqR5-rPoLQuew",
  "authDomain": "my-first-project-on-django.firebaseapp.com",
  "projectId": "my-first-project-on-django",
  "storageBucket": "my-first-project-on-django.appspot.com",
  "messagingSenderId": "698906702601",
  "appId": "1:698906702601:web:2290755529c923c0bad9d8",
  "measurementId": "G-4T2T4S0C5B",
  "databaseURL" : "https://my-first-project-on-django-default-rtdb.asia-southeast1.firebasedatabase.app/"

};

firebase = pyrebase.initialize_app(firebaseConfig)      

DataBase = firebase.database()
Auth = firebase.auth()
Storage = firebase.storage()


# Create your views here.

# Authentication

# SignUP
def signup(request):
    if request.method == 'POST':
        email = request.POST.get("signupUserEmail", '')
        password = request.POST.get("signupPassword", '')
        userName = request.POST.get("signupUserName")
        data = {"userName":userName, "userEmail":email, "userPassword":password}

        try:
            Auth.create_user_with_email_and_password(email, password) 
            DataBase.child("users").push(data)
            messages.success(request, 'Account Created Successfully. Please login.')
            return redirect('login')
        
        except Exception as e:
            error_message = str(e)
            if 'INVALID_EMAIL' in error_message:
                error_message = 'Invalid email address.'
            elif 'EMAIL_EXISTS' in error_message:
                error_message = 'Email address already exists.'
            messages.error(request, error_message)




    return render(request, 'signup.html')


# Login
def login(request):
    if request.method == 'POST':
        email = request.POST.get("loginUserEmail", '')
        password = request.POST.get("loginPassword", '')
        try:
            user = Auth.sign_in_with_email_and_password(email, password)
            request.session['user_id'] = user['localId']
            messages.success(request, 'Successfully Logged In.')
            return HttpResponseRedirect ('/auth/home/')
        except Exception as e:
            messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'login.html')