# Generated by Django 3.2.9 on 2021-12-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/avt.jpg', upload_to='avatar'),
        ),
    ]
