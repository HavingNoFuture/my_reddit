from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    """
    Дополненная базовая модель Django User.
    Поля username, email и password обязательны для создания экземпляра.
    """
    email = models.EmailField(_('email address'), unique=True)
    karma = models.IntegerField("Карма пользователя", default=0)
    about = models.TextField('О себе', default='', blank=True)
    phone_number = models.CharField('Номер телефона', max_length=12, default='', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    objects = CustomUserManager()

    def __str__(self):
        return self.username
