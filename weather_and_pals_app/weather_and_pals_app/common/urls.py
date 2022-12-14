from django.urls import path, include

from weather_and_pals_app.common.views import index, like_photo, comment_photo, favourite_city

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:pk>/', like_photo, name='like photo'),
    path('comment/<int:pk>/', comment_photo, name='comment photo'),
    path('favourite/<str:city_name>/', favourite_city, name='favourite city'),
)