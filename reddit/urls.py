from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='posts/'), name='main_page'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/add/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<str:slug>/comments/add/', views.comment_create_view, name='comment_create'),
]
