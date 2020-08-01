from django.urls import reverse_lazy
from django.views import generic

from reddit.forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    """Регистрация пользователя."""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
