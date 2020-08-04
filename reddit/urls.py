from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('posts/add/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
