from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from weather_and_pals_app.common.models import PhotoLike, PhotoComment, CityFavourite
from weather_and_pals_app.photos.models import Photo

UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'gender', 'email', 'profile_pic')
        field_classes = {'username': auth_forms.UsernameField, }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_not_required_fields()

    def __set_not_required_fields(self):
        for field_name, field in self.fields.items():

            field.required = False



class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {
            'username': auth_forms.UsernameField,
        }


