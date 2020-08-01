from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
