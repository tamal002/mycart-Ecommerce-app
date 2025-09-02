from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Add extra fields
    # since first_name, last_name, username, email, password already exists in django so we are not making those fields further

    def __str__(self):
        return self.username   