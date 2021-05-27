from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=240, verbose_name='Nombres')
    last_name = models.CharField(max_length=240, verbose_name='Apellidos')
    user_type = models.CharField(max_length=240, verbose_name='Tipo de usuario')