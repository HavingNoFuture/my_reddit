from django.contrib.auth import get_user_model
from django.views import generic

from .models import Post

User = get_user_model()


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
    queryset = Post.objects.all()


class PostCreateView(generic.CreateView):
    """Добавление нового поста"""
    model = Post
    fields = ('title', 'text')

    def form_valid(self, form):
        post = form.save(commit=False)
        user = self.request.user
        if user.is_authenticated:
            post.moderation = True
            post.author = user
        else:
            post.author = None
        post.save()
        return super().form_valid(form)

