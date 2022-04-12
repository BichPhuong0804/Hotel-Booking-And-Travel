from django.contrib import admin
from .models import Camnang2, Comment, Like

# Register your models here.
@admin.register(Camnang2)
class Camnang(admin.ModelAdmin):
    list_display = ('camnang_id', 'camnang_name', 'location', 'date', 'view',)
    search_fields = ('location', 'camnang_name',)
    
admin.site.register(Comment)
admin.site.register(Like)