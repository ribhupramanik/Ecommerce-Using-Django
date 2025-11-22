from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
        ('SELLER', 'Seller'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
