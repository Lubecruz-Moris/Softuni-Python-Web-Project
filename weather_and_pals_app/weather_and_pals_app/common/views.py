from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
import requests
import json
import os
from datetime import datetime

from weather_and_pals_app.common.forms import PhotoCommentForm
from weather_and_pals_app.common.models import PhotoLike, CityFavourite
from weather_and_pals_app.common.utils import get_photo_url, get_weather_update
from weather_and_pals_app.photos.models import Photo

UserModel = get_user_model()


def index(request):
    # if there are no errors the code inside try will execute
    try:
        # checking if the method is POST
        try:
            if request.method == 'POST':
                city_name = request.POST.get('city')
                city_search_weather_update = get_weather_update(city_name)

    # if the request method is GET empty the dictionary
            else:
                city_search_weather_update = {}

        except request.GET:
            city_search_weather_update = None
        user = UserModel.objects.filter(pk=request.user.pk).get()
        cities = CityFavourite.objects.filter(user=user).all()
        cities_favourite_weather_update = []
        for city in cities:
            city_favourite_weather_update = get_weather_update(city.city_name)
            cities_favourite_weather_update.append(city_favourite_weather_update)
        context = {'city_weather_update': city_search_weather_update,
           'cities_favourite_weather_update': cities_favourite_weather_update,
           }
        return render(request, 'common/home-page.html', context)


# if there is an error the 404 page will be rendered
# the except will catch all the errors
    except:
        return render(request, 'base/404.html')


@login_required
def favourite_city(request, pk):
    city = CityFavourite.objects.get(pk=pk)
    user = UserModel.objects.filter(pk=request.user.pk).get()
    user_city_favourites = CityFavourite.objects.filter(city_name=city.city_name, user=user)
    if user_city_favourites:
        user_city_favourites.delete()
    else:
        CityFavourite.objects.create(
            city_name=city.city_name,
            user_id=user.pk,
        )
    return redirect('index')


@login_required
def like_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    user = UserModel.objects.filter(pk=request.user.pk).get()
    user_liked_photos = PhotoLike.objects \
        .filter(photo=photo, user=user)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        PhotoLike.objects.create(
            photo=photo,
            user_id=user.pk,
        )

    return redirect(get_photo_url(request, pk))


@login_required
def comment_photo(request, pk):
    photo = Photo.objects.filter(pk=pk) \
        .get()
    user = UserModel.objects.filter(pk=request.user.pk).get()
    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)  # Does not persist to DB
        comment.photo = photo
        comment.user = user
        comment.save()

    return redirect(get_photo_url(request, pk))
