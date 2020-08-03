from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

from transliterate import translit


class Post(models.Model):
    """Модель поста."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    text = models.TextField("Текст")
    title = models.CharField("Название", max_length=150)
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    rating = models.IntegerField(default=0)
    moderation = models.BooleanField("Модерация пройдена?", default=False)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            try:
                self.slug = f"{int(self.pub_date.timestamp())}-{slugify(translit(self.title))}"
            except:
                self.slug = f"{int(self.pub_date.timestamp())}-{slugify(self.title)}"
            self.save(update_fields=("slug",))

    def __str__(self):
        return f'Post by {self.author.username}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


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
