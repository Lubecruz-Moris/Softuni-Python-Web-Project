
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather_and_pals_app.common.urls')),
    path('accounts/', include('weather_and_pals_app.accounts.urls')),
    path('photos/', include('weather_and_pals_app.photos.urls')),
]
