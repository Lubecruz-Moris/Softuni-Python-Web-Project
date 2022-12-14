from django.contrib import admin

from weather_and_pals_app.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'users')

    @staticmethod
    def users(current_photo_obj):
        tagged_users = current_photo_obj.tagged_users.all()
        if tagged_users:
            return ', '.join(u.username for u in tagged_users)
        return 'No tagged users'