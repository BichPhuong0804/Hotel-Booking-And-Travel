from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Img_slide(models.Model):
    img_id = models.AutoField(primary_key=True, unique=True, null=False)
    img = models.ImageField(max_length=100, default=None, upload_to='slide_hotel_img')
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE, default='')
     
    def __str__(self):
        return f"{self.img_id}"
    
class Firnish(models.Model):
    firnish_id = models.AutoField(primary_key=True, unique=True, null=False)
    firnish_name = models.CharField(max_length=100, default='') 
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE, default='')
    
    def __str__(self):
         return self.firnish_name
    
class Room(models.Model):
    room_id = models.AutoField(primary_key=True, unique=True, null=False)
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE, default='')
    room_name = models.CharField(max_length=100, default='') 
    price = models.FloatField(default=0)
    ROOM_VALUE = (
        ('1', 'Còn phòng'),
        ('0', 'Hết phòng'),
    )
    valu = models.CharField(choices=ROOM_VALUE, default='1', max_length=10)
    imga = models.ImageField(max_length=100, default=None, upload_to='room_img')
    
    def __str__(self):
        return self.room_name
    
class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True, unique=True, null=False)
    hotel_name = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    star = models.PositiveSmallIntegerField(default='')
    nearby = models.CharField(max_length=100, default='')
    map = models.URLField(max_length=1000, default='')
    phone = models.CharField(max_length=20, default='')
    image = models.ImageField(max_length=100, default=None, upload_to='hotel_img')
    description = models.TextField(default='')
    mprice = models.FloatField(default=0)
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)
    
    def __str__(self):
        return f"{self.hotel_id}"
    
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, unique=True, null=False)
    user = models.CharField(default='', max_length=100)
    hotel_id = models.CharField(default='', max_length=200)
    hname = models.CharField(max_length=500, default='')
    locate = models.CharField(max_length=100, default='')
    room_type = models.CharField(max_length=500, default='')
    room_id = models.CharField(max_length=500, default='')
    book_day = models.DateTimeField(default=timezone.now)
    check_in = models.DateField(default='')
    check_out = models.DateField(default='')
    quanti = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    cmnd = models.CharField(max_length=100, default='')
    pay = models.CharField(max_length=100, default='')
    total_price = models.CharField(max_length=100, default='')    
    
    def __str__(self):
        return f"{self.user} has booked {self.room_type} from {self.check_in} to {self.check_out}"
    
 
    

    
    
    
    