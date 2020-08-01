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
