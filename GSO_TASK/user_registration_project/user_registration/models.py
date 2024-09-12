# models.py

from django.db import models

class Hobby(models.Model):
    name = models.CharField(max_length=100)

class UserProfile(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dob = models.DateField()
    hobbies = models.ManyToManyField(Hobby)  # Many-to-many relationship for hobbies
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    remark = models.BooleanField()
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
