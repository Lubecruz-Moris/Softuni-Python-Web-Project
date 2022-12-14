from enum import Enum

from cloudinary import models as cloudinary_models
from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from weather_and_pals_app.core.model_mixins import ChoicesEnumMixin
from weather_and_pals_app.core.validators import validate_only_letters


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do no show'


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )
    profile_pic = cloudinary_models.CloudinaryField(
        default='https://res.cloudinary.com/djxufsuyv/image/upload/v1670784331/Default-welcomer_orc0jo.png',
        null=False,
        blank=True,

        )
