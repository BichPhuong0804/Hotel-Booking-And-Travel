from django import forms
from .models import Booking
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "booking_id",
            "user",
            "locate",
            "hotel_id",
            "hname", 
            "room_type",
            "room_id",
            "book_day",
            "check_in",
            "check_out",
            "name",
            "phone",
            "cmnd",
            "pay", 
            "total_price",
        ]
        
class BookingRoom(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "room_id",
            "room_type",
            "check_in",
            "check_out",
        ]
