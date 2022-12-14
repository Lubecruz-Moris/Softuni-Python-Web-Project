from django import forms

from weather_and_pals_app.common.models import PhotoLike, PhotoComment
from weather_and_pals_app.core.form_mixins import DisabledFormMixin
from weather_and_pals_app.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'user')


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo', 'user')


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_users.clear()

            Photo.objects.all() \
                .first().tagged_users.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id) \
                .delete()
            PhotoComment.objects.filter(photo_id=self.instance.id) \
                .delete()
            self.instance.delete()

        return self.instance