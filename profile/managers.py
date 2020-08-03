from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(UserManager):
    def create_user(self, email, username, password, **extra_fields):
        """
        Создает и сохраняет пользователя с заданными email, username и password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('The Username must be set'))

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
