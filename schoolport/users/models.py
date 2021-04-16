from http.client import CannotSendHeader
from django.contrib.auth.models import AbstractUser
from django.core.validators import BaseValidator
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, username, email, phone_number, password=None):
        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone_number = phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password):
        user = self.create_user(
            username,
            password=password,
            phone_number = phone_number,
            email=self.normalize_email(email),
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """Default user for schoolport."""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    username = models.CharField(max_length=255, unique=True)
    profile_photo = models.ImageField(blank=True)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone_number = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, choices=GENDER_CHOICES, max_length=100)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    #is_staff = models.BooleanField(default=False)

    # followers = models.ManyToManyField("self")
    # following = models.ManyToManyField("self")
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    # @property
    # def is_staff(self):
    #     return self.is_admin

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        