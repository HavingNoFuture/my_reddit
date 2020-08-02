from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from reddit.forms import CustomUserCreationForm, EditProfileForm


class SignUpView(generic.CreateView):
    """Регистрация пользователя."""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(LoginRequiredMixin, generic.View):
    """Страница профиля пользователя."""
    def get(self, request, *args, **kwargs):
        context = dict()
        context['user'] = request.user
        return render(request, 'reddit/user_profile.html', context)


class EditProfileView(LoginRequiredMixin, generic.View):
    """Редактирование профиля пользователя."""
    def get(self, request, *args, **kwargs):
        form = EditProfileForm(data=request.POST or None, user=request.user)
        context = dict()
        context['form'] = form
        return render(request, 'reddit/edit_profile.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        form = EditProfileForm(data=request.POST or None, user=user)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.phone_number = form.cleaned_data['phone_number']
            user.about = form.cleaned_data['about']
            user.save()
            return redirect(reverse('profile'))
        return self.get(request, *args, **kwargs)
