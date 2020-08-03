from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    """
    Измененная дефолтная модель создания юзера.
    Запрашивает email, username и password.
    """
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')


class EditProfileForm(forms.ModelForm):
    """
    Форма редактирования профиля пользователя.
    Автоматически вставляются данные пользователя в поля формы.
    """
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].widget.attrs.update({'value': user.first_name})
            self.fields['last_name'].widget.attrs.update({'value': user.last_name})
            self.fields['phone_number'].widget.attrs.update({'value': user.phone_number})
            self.fields['about'].widget.attrs.update({'value': user.about})

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'phone_number', 'about')
