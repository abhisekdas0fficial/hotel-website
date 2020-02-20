from django.shortcuts import render, redirect
from .form import UserForm, BookingForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = UserForm()
        return render(request, "registration/signup.html", {'form': form})


def check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)  # logs in the user
        return redirect("/home")
    else:
        return redirect("/login")


@login_required
def home(request):
    username = request.user.username
    return render(request, "home.html", {'username': username})


def logoutview(request):
    logout(request)  # logsout the current user
    return redirect("/login")
