from django import forms
from App_Posts.models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['images', 'caption']
