from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.CharField(default='', max_length=100)
    avatar = models.ImageField(default='avatar/avt.jpg', blank=True, null=True, upload_to='avatar')    
    def __str__(self):
        return str(self.user)  
    
