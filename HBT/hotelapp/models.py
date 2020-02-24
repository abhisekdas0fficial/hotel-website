from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HotelRoomsData(models.Model):
    name = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=200, null=True)
    image_path = models.CharField(max_length=30, null=True)
    price = models.PositiveIntegerField()


class UserBookingData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(
        HotelRoomsData, on_delete=models.CASCADE, null=True)
    phone_number = models.PositiveIntegerField()
    address = models.TextField(max_length=500, blank=False)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
