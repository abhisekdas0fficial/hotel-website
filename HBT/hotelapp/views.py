from django.shortcuts import render, redirect
from .models import HotelRoomsData
from .form import UserForm, BookingForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html', {'home_nav': 'active'})


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form': form})


def rooms(request):
    rooms = HotelRoomsData.objects.all()
    return render(request, "rooms.html", {'rooms': rooms, 'rooms_nav': 'active'})


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def register(request, id):
    room = HotelRoomsData.objects.get(id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.room_id = room
            instance.save()
            return redirect('/congrats')
    else:
        form = BookingForm()
    return render(request, 'registration/register.html', {'form': form, 'room': room})


@login_required
def congrats(request):
    return render(request, 'congrats.html')
