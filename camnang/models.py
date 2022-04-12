from django.db import models
from enum import unique
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User

# Create your models here.    
class Camnang2(models.Model):
    camnang_id = models.CharField(max_length=10, primary_key=True, unique=True, null=False, default='')
    camnang_name = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=100, default='')
    view = models.PositiveIntegerField(default=0)
    date = models.DateField()
    description = models.CharField(max_length=200, default='')
    bg = models.ImageField(max_length=100, default=None, upload_to='camnang_img')
    link = models.CharField(max_length=100, default='')
    liked = models.ManyToManyField(User, default=None, blank=True)
    
    def __str__(self):
        return self.camnang_id 
    
    @property
    def num_like(self):
        return self.liked.all().count()
    
class Comment(models.Model):
    user = models.CharField(max_length=200, default='')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post_id = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.post_id)
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_cn = models.CharField(max_length=200, default='')
    LIKE_CHOICES = (
        ('Like', 'Like'),
        ('Unlike', 'Unlike'),
    )
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.id_cn)