# Generated by Django 3.0.3 on 2020-02-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0004_userbookingdata_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelroomsdata',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='userbookingdata',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]