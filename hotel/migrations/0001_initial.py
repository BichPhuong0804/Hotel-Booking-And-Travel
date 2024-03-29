# Generated by Django 2.2.1 on 2021-12-18 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('hotel_name', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('star', models.PositiveSmallIntegerField(default='')),
                ('nearby', models.CharField(default='', max_length=100)),
                ('map', models.URLField(default='', max_length=1000)),
                ('phone', models.CharField(default='', max_length=20)),
                ('image', models.ImageField(default=None, upload_to='hotel_img')),
                ('description', models.TextField(default='')),
                ('mprice', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('room_name', models.CharField(default='', max_length=100)),
                ('price', models.FloatField(default=0)),
                ('valu', models.CharField(choices=[('1', 'Còn phòng'), ('0', 'Hết phòng')], default='1', max_length=10)),
                ('imga', models.ImageField(default=None, upload_to='room_img')),
                ('hotel_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hotel.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Img_slide',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('img', models.ImageField(default=None, upload_to='slide_hotel_img')),
                ('hotel_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hotel.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Firnish',
            fields=[
                ('firnish_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('firnish_name', models.CharField(default='', max_length=100)),
                ('hotel_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hotel.Hotel')),
            ],
        ),
    ]
