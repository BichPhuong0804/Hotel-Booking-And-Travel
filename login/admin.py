from django.contrib import admin

from login.models import Profile

# Register your models here.
@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    
