from django.contrib.auth import get_user_model
from django import template

from weather_and_pals_app.common.models import PhotoLike
register = template.Library()

@register.simple_tag
def apply_likes_count(photo):
    return photo.photolike_set.count()

@register.simple_tag
def apply_user_liked_photo(user, photo):
    # TODO: fix this for current user when authentication is available
    user_liked_photo = PhotoLike.objects.filter(photo=photo, user=user)
    # photo.is_liked_by_user = photo.likes_count > 0
    # return photo
    return user_liked_photo