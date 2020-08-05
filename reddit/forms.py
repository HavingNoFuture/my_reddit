from django import forms

from reddit.models import Comment


class CommentCreateForm(forms.ModelForm):
    """Форма создания нового комментария."""
    parent_comment = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )

    text = forms.CharField(
        label="",
        widget=forms.Textarea
    )

    class Meta:
        model = Comment
        fields = ('text',)