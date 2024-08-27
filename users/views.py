from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from users.forms import UserForm

# Create your views here.

def login_page(request) :
    return render(request, 'users/login.html') 


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, "users/login.html")
    else:
        form = UserForm()
    return render(request, "users/signup.html", {"form": form})