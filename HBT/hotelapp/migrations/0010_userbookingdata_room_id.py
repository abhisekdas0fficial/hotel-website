# Generated by Django 3.0.3 on 2020-02-23 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0009_auto_20200222_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbookingdata',
            name='room_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelapp.HotelRoomsData'),
        ),
    ]
