from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .managers import CustomUserManager


class User(AbstractUser):
    """
    Дополненная базовая модель Django User.
    Поля username, email и password обязательны для создания экземпляра.
    """
    email = models.EmailField(_('email address'), unique=True)
    karma = models.IntegerField("Карма пользователя", default=0)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Post(models.Model):
    """Модель поста."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    text = models.TextField("Текст")
    title = models.CharField("Название", max_length=150)
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    rating = models.IntegerField(default=0)
    moderation = models.BooleanField("Модерация пройдена?", default=False)

    def __str__(self):
        return f'Post by {self.author.username}'


class Comment(models.Model):
    """Модель комментария. Имеет рекурсию на саму себя."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    text = models.TextField("Текст")
    karma = models.IntegerField("Карма пользователя", default=0)
    moderation = models.BooleanField("Модерация пройдена?", default=False)
    parent = models.ForeignKey(
        "self", verbose_name="Родитель", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f'Comment by {self.author.username}'
