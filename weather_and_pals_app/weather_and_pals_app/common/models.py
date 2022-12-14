from django.contrib.auth import get_user_model
from django.db import models

from weather_and_pals_app.photos.models import Photo

UserModel = get_user_model()


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=True,
        blank=True,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class PhotoLike(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class CityFavourite(models.Model):
    CITY_MAX_LEN = 25
    city_name = models.CharField(
        max_length=CITY_MAX_LEN,
        null=False,
        blank=False,
        )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )