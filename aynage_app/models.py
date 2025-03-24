from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
            
    def __str__(self):
        return f"{self.username}"
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(default = 1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    STATUS_CHOICES = [
        (1, 'Published'),
        (0, 'Unpublished'),
    ]
    
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('fashion', 'Fashion'),
        ('help', 'Help'),
        ('ngo', 'NGO'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    banner = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Vacancy(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(default = 1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name