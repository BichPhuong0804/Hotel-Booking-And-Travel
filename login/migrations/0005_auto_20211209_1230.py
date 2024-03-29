# Generated by Django 3.2.9 on 2021-12-09 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0004_auto_20211209_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250, null=True)),
                ('fullname', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('avatar', models.ImageField(blank=True, default=None, upload_to='media/avatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='register_tables',
            name='user',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
        migrations.DeleteModel(
            name='Register_tables',
        ),
    ]
