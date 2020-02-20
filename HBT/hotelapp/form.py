from django import forms
from .models import UserBookingData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class BookingForm(forms.ModelForm):
    class Meta:
        model = UserBookingData
        fields = ('address', 'check_in_date', 'check_out_date')
