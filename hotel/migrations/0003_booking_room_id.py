# Generated by Django 2.2.1 on 2021-12-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='room_id',
            field=models.CharField(default='', max_length=500),
        ),
    ]
