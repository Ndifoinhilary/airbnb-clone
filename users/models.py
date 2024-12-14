from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    """
    Customer user model
    """
    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_FRENCH = 'fr'
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'
    CURRENCY_DOLLARS = 'USD'
    CURRENCY_EUR = 'EUR'
    CURRENCY_CHOICES = (

    )
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_FRENCH, 'French'),
    )
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_FEMALE, 'Other'),
    )

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default=GENDER_MALE)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=7, choices=LANGUAGE_CHOICES, default=LANGUAGE_ENGLISH)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=CURRENCY_DOLLARS)
    superhost = models.BooleanField(default=False)

