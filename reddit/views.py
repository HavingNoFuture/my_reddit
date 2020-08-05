from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.views.decorators.http import require_http_methods

from .forms import CommentCreateForm
from .models import Post, Comment

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

    def get_context_data(self, **kwargs):
        kwargs['comment_form'] = CommentCreateForm(data=self.request.POST or None)
        return super().get_context_data(**kwargs)


class PostCreateView(generic.CreateView):
    """Добавление нового поста"""
    model = Post
    fields = ('title', 'text')

    def form_valid(self, form):
        post = form.save(commit=False)
        user = self.request.user
        if user.is_authenticated:
            post.author = user
            post.moderation = True
        else:
            post.author = None
        post.save()
        return super().form_valid(form)


@require_http_methods(["POST"])
def comment_create_view(request, slug):
    """Создание нового комментария"""
    form = CommentCreateForm(request.POST)
    post = get_object_or_404(Post, slug=slug)

    if form.is_valid():
        comment = form.save(commit=False)
        user = request.user
        if user.is_authenticated:
            comment.author = user
            comment.moderation = True
        else:
            comment.author = None
        comment.post = post
        comment.save()

        try:
            comment_id = form.cleaned_data['parent_comment']
            comment.path.extend(Comment.objects.get(id=comment_id).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)

        comment.save(update_fields=('path',))
    return redirect(post.get_absolute_url())
