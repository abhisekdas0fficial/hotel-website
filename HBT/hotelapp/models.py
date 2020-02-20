from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserBookingData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
