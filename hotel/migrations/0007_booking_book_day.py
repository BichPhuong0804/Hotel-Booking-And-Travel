# Generated by Django 2.2.1 on 2021-12-18 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20211219_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='book_day',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
