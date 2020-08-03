from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.ProfileView.as_view(), name='profile'),
    path('edit/', views.EditProfileView.as_view(), name='edit_profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]