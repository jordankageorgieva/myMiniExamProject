from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from profiles.managers import AppUserManager


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2),
                    RegexValidator(regex=r'^[A-Za-z0-9_]+$',
                    message="Ensure this value contains only letters, numbers, and underscore.")],
    )
    email = models.EmailField()
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    objects = AppUserManager()

