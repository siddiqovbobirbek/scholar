from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.dispatch import receiver



class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    job = models.CharField(max_length=200)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
