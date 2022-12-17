from django.contrib import admin

from django.contrib import admin

from weather_and_pals_app.common.models import PhotoComment, CityFavourite


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'photo', 'user')


@admin.register(CityFavourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'city_name', 'user')

