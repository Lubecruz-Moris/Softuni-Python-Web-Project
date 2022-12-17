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


class PhotoDeleteForm(PhotoBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

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
    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.required = False
            field.widget.attrs['disabled'] = True