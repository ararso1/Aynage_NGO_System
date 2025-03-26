from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.

class User(AbstractUser):
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
            
    def __str__(self):
        return f"{self.username}"
    
""" class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(default = 1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name """
    
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
    description = RichTextField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    banner = models.ImageField(upload_to='images/')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Auto-updates on every save
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='blogs_added')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='blogs_updated')

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
    ]

    STATUS_CHOICES = [
        (1, 'Published'),
        (0, 'Unpublished'),
    ]

    title = models.CharField(max_length=250)
    department = models.CharField(max_length=250, default="General")
    experience = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=20, default='full_time', choices=JOB_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, default='Silte')
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    banner = models.ImageField(upload_to='images/', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    deadline = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vacancy_added')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vacancy_updated')

    def __str__(self):
        return self.title
