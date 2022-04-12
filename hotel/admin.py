from django.contrib import admin
from .models import Hotel, Img_slide, Room, Firnish, Booking

# Register your models here.
@admin.register(Hotel)
class Hotel(admin.ModelAdmin):
    list_display = ('hotel_id', 'hotel_name', 'location', 'address', 'star', 'mprice')
    search_fields = ('hotel_id', 'hotel_name', 'location', 'star', 'mprice')
    
@admin.register(Img_slide)
class Img_silde(admin.ModelAdmin):
    list_display = ('hotel_id','img_id', 'img')
    search_fields = ('hotel_id',)
    
@admin.register(Room)
class Room(admin.ModelAdmin):
    list_display = ('hotel_id', 'room_id', 'room_name', 'valu', 'price')
    search_fields = ('room_name', 'hotel_id','price' )
    
@admin.register(Firnish)
class Firnish(admin.ModelAdmin):
    list_display = ('hotel_id','firnish_id', 'firnish_name')
    search_fields = ('firnish_name', 'hotel_id')

@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = ('booking_id', 'user', 'hotel_id', 'hname', 'room_type', 'pay')
