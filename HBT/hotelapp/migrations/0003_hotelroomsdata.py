# Generated by Django 3.0.3 on 2020-02-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0002_auto_20200220_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRoomsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
