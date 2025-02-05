from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for users to comment on a published event 
    """
    class Meta:
        model = Comment
        fields = ('content',)
