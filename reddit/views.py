from django.views import generic

from .models import Post


# Post views
class PostListView(generic.ListView):
    """Список постов"""
    model = Post
    queryset = Post.objects.filter(moderation=True)
    ordering = ("-pub_date",)
    paginate_by = 3


class PostDetailView(generic.DetailView):
    """Детали поста"""
    model = Post
    queryset = Post.objects.filter(moderation=True)
