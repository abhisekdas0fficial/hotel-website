# Generated by Django 3.0.3 on 2020-02-22 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0007_auto_20200222_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbookingdata',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userbookingdata',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='userbookingdata',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
