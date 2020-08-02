from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', include('django.contrib.auth.urls')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.EditProfileView.as_view(), name='edit_profile'),
    path('profile/signup/', views.SignUpView.as_view(), name='signup'),
]