from django import forms
from tool_03.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name','content','blog_id']
