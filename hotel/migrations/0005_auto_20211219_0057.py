# Generated by Django 2.2.1 on 2021-12-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_booking_quanti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
    ]
