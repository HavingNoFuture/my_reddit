from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

from transliterate import translit


class Post(models.Model):
    """Модель поста."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор",
                               on_delete=models.SET_NULL, null=True)
    title = models.CharField("Название", max_length=150)
    text = models.TextField("Текст")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    rating = models.IntegerField(default=0)
    moderation = models.BooleanField("Модерация пройдена?", default=False)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        """
        Расширяет станадартный save() модели.
        При сохранение экземпляра поста автоматически генерирует slug
        на основе pub_date и title.
        pub_date конвертируется в секунды с 1970.
        Из title делается слаг. Если title на русском - берется транслит и затем делается слаг.
        For example:
            pub_date: Aug. 3, 2020, 1:30 p.m
            title: Title
            -> 1596461449-title
        """
        super().save(*args, **kwargs)
        if not self.slug:
            try:
                self.slug = f"{int(self.pub_date.timestamp())}-{slugify(translit(self.title))}"
            except:
                self.slug = f"{int(self.pub_date.timestamp())}-{slugify(self.title)}"
            self.save(update_fields=("slug",))

    def __str__(self):
        if self.author is None:
            return 'Anonymous Post'
        return f'Post by {self.author}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    """Модель комментария. Имеет рекурсию на саму себя."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    text = models.TextField("Текст")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    karma = models.IntegerField("Карма пользователя", default=0)
    moderation = models.BooleanField("Модерация пройдена?", default=False)
    parent = models.ForeignKey(
        "self", verbose_name="Родитель", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        if self.author is None:
            return 'Anonymous Comment'
        return f'Comment by {self.author}'
