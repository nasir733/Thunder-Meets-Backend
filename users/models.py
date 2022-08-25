from statistics import mode

from django.contrib.humanize.templatetags import humanize
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from core.models import CoreModel
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from simple_history.models import HistoricalRecords
from django_extensions.db.fields import AutoSlugField
from django_countries.fields import CountryField
from django.db import models

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

def get_profile_image_filepath(self, filename):
    return "avatars/" + str(self.pk) + "/avatar.png"


def get_default_profile_image():
    return "room_photos/1.webp"

class User(AbstractBaseUser, PermissionsMixin, CoreModel):
    """User Model"""

    GENDER_CHOICES = (
        ("male", "male"),
        ("female", "female"),
        ("non-binary","non-binary"),
    )
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['first_name', 'last_name','email'], unique=True)
    country = CountryField(null=True,blank=True)
    phone_no = PhoneNumberField(blank=True,null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()


    username = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        max_length=255,
        upload_to=get_profile_image_filepath,
        null=True,
        blank=True,
        default=get_default_profile_image,
    )


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = UserAccountManager()

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email


